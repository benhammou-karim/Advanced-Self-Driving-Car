"""
This file contains unit test for Motor class

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
import motor

class TestMotor(unittest.TestCase):
    """
    A class containing unit tests for the Motor Class.
    """
    def setUp(self):
        # Set up the GPIO module for testing
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def testSetUpMotor(self):
        """
        test setUpMotor function
        """
        # create a Motor object with mock GPIO pins
        motor1 = motor.Motor(enableGpio=18, input1Gpio=23, input2Gpio=24)
        # create mock GPIO
        MGPIO = MagicMock()
        motor1.GPIO = MGPIO
        # call setUpMotor to set up the motor
        motor1.setUpMotor()
        # check that the GPIO pins are set up correctly
        self.assertEqual(GPIO.gpio_function(motor1.enableGpio), GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(motor1.input1Gpio), GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(motor1.input2Gpio), GPIO.OUT)
    def testStartMotor(self):
        """
        test startMotor function
        """
        motor1 = motor.Motor(enableGpio=18, input1Gpio=23, input2Gpio=24)
        # create mock GPIO
        MGPIO = MagicMock()
        motor.GPIO = MGPIO
        # call startMotor()
        motor1.startMotor()
        pwm = MGPIO.PWM(motor1.enableGpio, 1000)
        # test start pwm is called with enableGpio
        pwm.start.assert_called_with(motor1.enableGpio)
        # test duty cycle is set to 50
        pwm.ChangeDutyCycle.assert_called_with(50)
    def testForward(self):
        """
        test forward function
        """
        motor1 = motor.Motor(enableGpio=18, input1Gpio=23, input2Gpio=24)
        # create mock GPIO
        MGPIO = MagicMock()
        motor.GPIO = MGPIO
        # Call forward
        motor1.forward()
        # test output of input1Gpio is set to LOW
        MGPIO.output.assert_any_call(motor1.input1Gpio, MGPIO.LOW)
        # test output of input2Gpio is set to HIGH
        MGPIO.output.assert_any_call(motor1.input2Gpio, MGPIO.HIGH)
    def testBackward(self):
        """
        test backward function
        """
        motor1 = motor.Motor(enableGpio=18, input1Gpio=23, input2Gpio=24)
        # create mock GPIO
        MGPIO = MagicMock()
        motor.GPIO = MGPIO
        # Call backward
        motor1.backward()
        # test output of input1Gpio is set to HIGH
        MGPIO.output.assert_any_call(motor1.input1Gpio, MGPIO.HIGH)
        # test output of input2Gpio is set to LOW
        MGPIO.output.assert_any_call(motor1.input2Gpio, MGPIO.LOW)
    def testStopMotor(self):
        """
        test stopMotor function
        """
        motor1 = motor.Motor(enableGpio=18, input1Gpio=23, input2Gpio=24)
        # create mock GPIO
        MGPIO = MagicMock()
        motor.GPIO = MGPIO
        # Call stopMotor
        motor1.stopMotor()
        # test output of input1Gpio is set to LOW
        MGPIO.output.assert_any_call(motor1.input1Gpio, MGPIO.LOW)
        # test output of input2Gpio is set to LOW
        MGPIO.output.assert_any_call(motor1.input2Gpio, MGPIO.LOW)
    def testSlowDownMotor(self):
        """
        test slowDownMotor function
        """
        motor1 = motor.Motor(enableGpio=18, input1Gpio=23, input2Gpio=24)
        # create mock GPIO
        MGPIO = MagicMock()
        motor.GPIO = MGPIO
        # Call slowDownMotor
        motor1.slowDownMotor()
        # test duty cycle is changed to 50
        motor1.pwm.ChangeDutyCycle.assert_called_with(50)
    def testSpeedUpMotor(self):
        """
        test speedUpMotor function
        """
        motor1 = motor.Motor(enableGpio=18, input1Gpio=23, input2Gpio=24)
        # create mock GPIO
        MGPIO = MagicMock()
        motor.GPIO = MGPIO
        # Call speedUpMotor
        motor1.speedUpMotor()
        # test duty cycle is changed to 100
        motor1.pwm.ChangeDutyCycle.assert_called_with(100)
    def testSetToMediumSpeed(self):
        """
        test setToMediumSpeed function
        """
        motor1 = motor.Motor(enableGpio=18, input1Gpio=23, input2Gpio=24)
        MGPIO = MagicMock()
        motor.GPIO = MGPIO
        # Call setToMediumSpeed
        motor1.setToMediumSpeed()
        # test duty cycle is changed to 75
        motor1.pwm.ChangeDutyCycle.assert_called_with(75)

if __name__ == "__main__":
     unittest.main()