import RPi.GPIO as GPIO
from hx711 import HX711

# Configuration du GPIO pour la lampe rouge
RED_LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN, GPIO.OUT)

# Configuration du module HX711 pour le capteur de poids
hx = HX711(dout_pin=5, pd_sck_pin=6)
hx.set_reading_format("MSB")
hx.set_reference_unit(1)  # Modifier la référence en fonction de votre calibrage
hx.reset()
hx.tare()

# Fonction pour allumer ou éteindre la lampe rouge
def controler_lampe(activation):
    if activation:
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(RED_LED_PIN, GPIO.LOW)

# Boucle principale de mesure du poids
while True:
    try:
        poids = hx.get_weight_mean(10)  # Moyenne des mesures pour une meilleure précision
        hx.power_down()
        hx.power_up()

        if poids > 600:
            controler_lampe(True)
        else:
            controler_lampe(False)

        print("Poids : {} g".format(poids))

    except (KeyboardInterrupt, SystemExit):
        GPIO.cleanup()
        raise