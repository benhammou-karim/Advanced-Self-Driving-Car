"""
This file contains unit test for Detector (empty) class

Author: Abdessalam BOULAYAT
"""
import unittest
from unittest.mock import MagicMock
import sys
sys.path.append("..")
# import detector module
import detectVide

class TestDetectVide(unittest.TestCase):
    """
    A class containing unit tests for the Detector(empty) Class.
    """
    def testSetupDetector(self):
        """
        test setupDetector function
        """
        detectorVide = detectVide.DetectorEmpty(trigGpio=23, echoGpio=24)
        # create mock GPIO
        MGPIO = MagicMock()
        detectorVide.GPIO = MGPIO
        # call setupDetector
        detectorVide.setupDetector()
        # check that the GPIO pins are set up correctly
        MGPIO.setup.assert_called_with(detectorVide.trigGpio, MGPIO.OUT)
        MGPIO.setup.assert_called_with(detectorVide.echoGpio, MGPIO.IN)
        MGPIO.output.assert_called_with(detectorVide.trigGpio, False)
    
    def testStop(self):
        """
        test function stop detector
        """
        detectorVide = detectVide.DetectorEmpty(trigGpio=23, echoGpio=24)
        # create mock gpio
        MGPIO = MagicMock()
        detectorVide.GPIO = MGPIO
        # call function stop detector
        detectorVide.stop()
        # test si le thread detector est arrêtée
        self.assertFalse(detectorVide.is_alive())
    def testIsEven(self):
        """
        test is_even function
        """
        detectorVide = detectVide.DetectorEmpty(trigGpio=23, echoGpio=24)
        # create mock gpio
        MGPIO = MagicMock()
        detectorVide.GPIO = MGPIO
        # call is_even
        # when number is even
        self.assertTrue(detectorVide.is_even(2))
        # when number is not even
        self.assertFalse(detectorVide.is_even(3))

if __name__ == "__main__":
     unittest.main()
        