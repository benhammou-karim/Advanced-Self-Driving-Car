import unittest
from unittest.mock import MagicMock, call
# import lineSensor module
import lineSensor

class TestLineSensor(unittest.TestCase):

    def testSetupLineSensor(self):
        """
        test setupLinseSensor function
        """
        lineSensor1 = lineSensor.LineSensor(outGpioRight=26,outGpioLeft=22)
        # create mock GPIO
        MGPIO = MagicMock()
        lineSensor.GPIO = MGPIO
        # call setupLineSensor
        lineSensor1.setupLineSensor()
        # Check that the GPIO pins are set up correctly
        expected_calls = [
            call(lineSensor1.outGpioLeft, MGPIO.IN),
            call(lineSensor1.outGpioRight, MGPIO.IN)
        ]
        MGPIO.setup.assert_has_calls(expected_calls)
    def testStop(self):
        """
        test stop lineSensor
        """
        lineSensor1 = lineSensor.LineSensor(outGpioRight=26,outGpioLeft=22)
        # create mock GPIO
        MGPIO = MagicMock()
        lineSensor.GPIO = MGPIO
        # call stop
        lineSensor1.stop()
        # test if lineSensor is stoped
        self.assertFalse(lineSensor1.is_alive())
if __name__ == "__main__":
     unittest.main()
