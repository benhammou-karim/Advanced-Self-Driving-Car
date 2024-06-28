"""
This file contains unit test for Car class

Author: Abdessalam BOULAYAT
"""
import unittest
from unittest.mock import MagicMock
import sys
sys.path.append("..")
# import car module to test its functions
from car import Car
from led import Led
from motor import Motor
from detector import Detector

class TestCar(unittest.TestCase):
    """
    A class containing unit tests for the Car Class.
    """
    def testStop(self):
        """
        test stop car
        """
        # create mock led
        led = MagicMock()
        # create mock detector
        detector = MagicMock()
        # create mock motors
        motor_left = MagicMock()
        motor_right = MagicMock()
        car = Car(led, detector, motor_left, motor_right)
        # call stop
        car.stop()
        # test detector is stopped
        self.assertTrue(car.detector.stop_event.is_set())
        # test led is off
        led.turnOffLed.assert_called_once()
        # test if motors are stopped
        motor_left.stopMotor.assert_called_once()
        motor_right.stopMotor.assert_called_once()
        # test thread car is stopped
        self.assertTrue(car.stop_event.is_set())
    def testForward(self):
        """
        test forward function
        """
        # create mock led
        led = MagicMock()
        # create mock detector
        detector = MagicMock()
        # create mock motors
        motor_left = MagicMock()
        motor_right = MagicMock()
        car = Car(led, detector, motor_left, motor_right)
        # call forward
        car.forward()
        # test if motors are going forward
        motor_left.forward.assert_called_once()
        motor_right.forward.assert_called_once()
    def testBackward(self):
        """
        test forward function
        """
        # create mock led
        led = MagicMock()
        # create mock detector
        detector = MagicMock()
        # create mock motors
        motor_left = MagicMock()
        motor_right = MagicMock()
        car = Car(led, detector, motor_left, motor_right)
        # call backward
        car.backward()
        # test if motors are going backward
        motor_left.backward.assert_called_once()
        motor_right.backward.assert_called_once()
    def testStopCar(self):
        """
        test stopCar function
        """
        # create mock led
        led = MagicMock()
        # create mock detector
        detector = MagicMock()
        # create mock motors
        motor_left = MagicMock()
        motor_right = MagicMock()
        car = Car(led, detector, motor_left, motor_right)
        # call stop
        car.stopCar()
        # test if motors are stopped
        motor_left.stopMotor.assert_called_once()
        motor_right.stopMotor.assert_called_once()
    def testTurnRight(self):
        """
        test turnRight function
        """
        # create mock led
        led = MagicMock()
        # create mock detector
        detector = MagicMock()
        # create mock motors
        motor_left = MagicMock()
        motor_right = MagicMock()
        car = Car(led, detector, motor_left, motor_right)
        # call turnRight
        car.turnRight()
        # test if motor_lef is forward and motor_right backward
        motor_left.forward.assert_called_once()
        motor_right.stopMotor.assert_called_once()
    def testTurnLeft(self):
        """
        test turnLeft function
        """
        # create mock led
        led = MagicMock()
        # create mock detector
        detector = MagicMock()
        # create mock motors
        motor_left = MagicMock()
        motor_right = MagicMock()
        car = Car(led, detector, motor_left, motor_right)
        # call turnRight
        car.turnLetf()
        # test if motor_right is forward and motor_left backward
        motor_left.stopMotor.assert_called_once()
        motor_right.forward.assert_called_once()
    def testSlowDownCar(self):
        """
        test slowDownCar function
        """
        # create mock led
        led = MagicMock()
        # create mock detector
        detector = MagicMock()
        # create mock motors
        motor_left = MagicMock()
        motor_right = MagicMock()
        car = Car(led, detector, motor_left, motor_right)
        # call turnRight
        car.slowDownCar()
        # test if motors are slowDown
        motor_left.slowDownMotor.assert_called_once()
        motor_right.slowDownMotor.assert_called_once()
    def testSpeedUpCar(self):
        """
        test speedUpCar function
        """
        # create mock led
        led = MagicMock()
        # create mock detector
        detector = MagicMock()
        # create mock motors
        motor_left = MagicMock()
        motor_right = MagicMock()
        car = Car(led, detector, motor_left, motor_right)
        # call turnRight
        car.speedUpCar()
        # test if motors are speedUp
        motor_left.speedUpMotor.assert_called_once()
        motor_right.speedUpMotor.assert_called_once()
    def mediumUpCar(self):
        """
        test mediumUpCar function
        """
        # create mock led
        led = MagicMock()
        # create mock detector
        detector = MagicMock()
        # create mock motors
        motor_left = MagicMock()
        motor_right = MagicMock()
        car = Car(led, detector, motor_left, motor_right)
        # call mediumUpCar
        car.mediumUpCar()
        # test if motors are set to medium speed
        motor_left.setToMediumSpeed.assert_called_once()
        motor_right.setToMediumSpeed.assert_called_once()
    
if __name__ == "__main__":
    unittest.main()