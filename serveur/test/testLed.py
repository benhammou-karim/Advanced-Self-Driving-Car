"""
This file contains unit test for Led class

Author: Abdessalam BOULAYAT
"""
import unittest
from unittest.mock import MagicMock
import sys
sys.path.append("..")
import fake_rpi
sys.modules["RPi"] = fake_rpi.RPi
sys.modules["RPi.GPIO"] = fake_rpi.RPi.GPIO
import RPi.GPIO as GPIO
# import led module
import led

class TestLed(unittest.TestCase):
    
    """
    A class containing unit tests for the Led Class.
    """
    def testSetUpLed(self):
        """
        Test function setUpLed()
        """
        led1 = led.Led(ledGpio=18)
        # create mock GPIO
        MGPIO = MagicMock()
        led1.GPIO = MGPIO

        led1.setUpLed()
        # test GPIO mode is set to BCM
        self.assertEqual(led.GPIO.getmode(), GPIO.BCM)
        # test ledGpio is set as an output
        self.assertEqual(GPIO.gpio_function(led1.ledGpio), GPIO.OUT)

    def testTurnOnLed(self):
        led1 = led.Led(ledGpio=18)
        # create mock GPIO
        MGPIO = MagicMock()
        led.GPIO = MGPIO
        led1.turnOnLed()
        # test ledGpio output is set to HIGH
        MGPIO.output.assert_called_once_with(led1.ledGpio, MGPIO.HIGH)
    
    def testTurnOffLed(self):
        led1 = led.Led(ledGpio=18)
        # create mock GPIO
        MGPIO = MagicMock()
        led.GPIO = MGPIO
        led1.turnOffLed()
        # test ledGpio output is set to HIGH
        MGPIO.output.assert_called_once_with(led1.ledGpio, MGPIO.LOW)
    
if __name__ == "__main__":
     unittest.main()