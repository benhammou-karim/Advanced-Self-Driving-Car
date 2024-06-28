"""
This file contains unit test for Detector class

Author: Abdessalam BOULAYAT
"""
import unittest
from unittest.mock import MagicMock
import sys
sys.path.append("..")
# import detector module
import detector

class TestDetector(unittest.TestCase):
    """
    A class containing unit tests for the Detector Class.
    """
    def testSetupDetector(self):
        """
        test setupDetector function
        """
        detector1 = detector.Detector(trigGpio=23, echoGpio=24)
        # create mock GPIO
        MGPIO = MagicMock()
        detector.GPIO = MGPIO
        # call setupDetector
        detector1.setupDetector()
        # check that the GPIO pins are set up correctly
        #MGPIO.setup.assert_called_with(detector1.trigGpio, MGPIO.OUT)
        MGPIO.setup.assert_called_with(detector1.echoGpio, MGPIO.IN)
        MGPIO.output.assert_called_with(detector1.trigGpio, False)
        #self.assertEqual(GPIO.gpio_function(detector1.input2Gpio), GPIO.OUT)
    def testStop(self):
        """
        test stop detector
        """
        detector1 = detector.Detector(trigGpio=23, echoGpio=24)
        # create mock GPIO
        MGPIO = MagicMock()
        detector.GPIO = MGPIO
        # call stop
        detector1.stop()
        # test si le thread detector est arrêtée
        self.assertFalse(detector1.is_alive())
    def testIsEven(self):
        """
        test is_even function
        """
        detector1 = detector.Detector(trigGpio=23, echoGpio=24)
        # create mock GPIO
        MGPIO = MagicMock()
        detector.GPIO = MGPIO
        # call is_even
        # when number is even
        self.assertTrue(detector1.is_even(2))
        # when number is not even
        self.assertFalse(detector1.is_even(3))

if __name__ == "__main__":
     unittest.main()