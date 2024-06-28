"""
This file contains class representing an LED and its behavior.
Author: Imad AHDDAD
"""
import RPi.GPIO as GPIO
class Led:
    """
    A class representing an LED connected to a car.

    Attributes:
    ----------
    **ledGpio (int):** 
        the GPIO pin number to which the LED is connected  

    Methods:
    **__init__(self, ledGpio):** 
        Constructor for the Led class  
    **setUpLed(self):** 
        Initializes the GPIO pins and sets up the LED for use  
    **turnOnLed(self):** 
        Turns ON the LED  
    **turnOffLed(self):** 
        Turns OFF the LED  
    """
    def __init__(self, ledGpio):  
        """
        Constructor for the Led class.

        Args:
        **ledGpio (int):** 
            the GPIO pin number to which the LED is connected  
        """  
        GPIO.setwarnings(False)
        self.ledGpio = ledGpio
        self.setUpLed()
    
    def setUpLed(self):
        """
        This method initializes the GPIO pins and sets up the LED for use
        """        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ledGpio,GPIO.OUT)

    def turnOnLed(self):
        """
        This method turns ON the LED
        """        
        GPIO.output(self.ledGpio,GPIO.HIGH)

    def turnOffLed(self):
        """
        This method turns OFF the LED
        """ 
        GPIO.output(self.ledGpio,GPIO.LOW)
        