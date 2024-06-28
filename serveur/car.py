"""
This file contains class representing a car Thread and its behavior.
Author: Imad AHDDAD
"""
import threading
from led import Led
from detector import Detector
from motor import Motor
from lineSensor import LineSensor
from detectVide import DetectorEmpty

class Car(threading.Thread):
    """
    A class representing a car Thread and its behavior.

    Attributes
    ----------
    **stop_event (threading.Event):** 
        An event that is used to signal when the thread should stop running  
    **motorDirection (int):** 
        An integer representing the current direction of the car's motors (-1 for backward, 0 for stop, 1 for forward)  
    **action (str):** 
        A string representing the current action to be performed by the car (e.g. 'f' for forward, 'b' for backward)  
    **motor_left (Motor):** 
        A Motor object representing the left motor of the car  
    **motor_right (Motor):** 
        A Motor object representing the right motor of the car  
    **led (Led):** 
        A Led object representing the LED attached to the car  
    **detector (Detector):** 
        A Detector object representing the obstacle detector attached to the car  

    Methods
    -------
    **run():** 
        The main method that gets executed when the thread is started  
    **stop():**
        Stops the thread and performs cleanup tasks (e.g. stops the detector thread, turns off the LED, stops the motors)  
    **forward():** 
        Makes the car go forward  
    **backward():** 
        Makes the car go backward  
    **stopCar():** 
        Stops the car  
    **turnRight():** 
        Turns the car to the right  
    **turnLeft():** 
        Turns the car to the left  
    **slowDownCar():** 
        Slows down the car  
    **speedUpCar():** 
        Speeds up the car  
    **mediumUpCar():** 
        Sets the car's speed to medium  
    """
    def __init__(self, led: Led, detector: Detector, motor_left: Motor, motor_right: Motor, detectorEmpty: DetectorEmpty, lineSensor:LineSensor):
        """
        Constructor for Car class.

        Args:
        **led (Led):** 
            the object representing the LED attached to the car  
        **detector (Detector):** 
            the object representing the obstacle detector attached to the car  
        **motor_left (Motor):** 
            A Motor object representing the left motor of the car  
        **motor_right (Motor):** 
            A Motor object representing the right motor of the car  
        """
        super().__init__()
        self.stop_event = threading.Event()
        self.motorDirection = 0
        self.action = 'z'
        self.motor_left = motor_left
        self.motor_right = motor_right
        self.led = led
        self.detector = detector
        self.detector.car = self
        self.detectorEmpty = detectorEmpty
        self.detectorEmpty.car = self
        self.lineSensor = lineSensor
        self.lineSensor.car = self
        print("the car thread created")
    def startCar(self):
        self.isRun = True
        if(self.detector.is_alive() == False):
            self.detector.stop_event.clear()
            self.detector = Detector(trigGpio=23, echoGpio=24)
            self.detector.car = self
            self.detector.start()
        if(self.detectorEmpty.is_alive() == False):
            self.detectorEmpty.stop_event.clear()
            self.detectorEmpty = DetectorEmpty(trigGpio=17, echoGpio=27)
            self.detectorEmpty.car = self
            self.detectorEmpty.start()
        if(self.lineSensor.is_alive() == False):
            self.lineSensor.stop_event.clear()
            self.lineSensor = LineSensor(outGpioRight=22,outGpioLeft=26)
            self.lineSensor.car = self
            self.lineSensor.start()
    def stop(self):
        """
        this methods stops the thread
        """ 
        # stop the detector thread if it's alive
        if(self.detector.is_alive()):
            self.detector.stop()
        if(self.detectorEmpty.is_alive() == True):
            self.detectorEmpty.stop()
        if(self.lineSensor.is_alive() == True):
            self.lineSensor.stop()
        # turn of the led
        self.led.turnOffLed()
        # stop motors
        self.motor_left.stopMotor()
        self.motor_right.stopMotor()
        #stop thread
        self.stop_event.set()
        print('\033[91m' + 'The car thread is stopped' + '\033[0m')
    def forward(self):
        """
        This method makes the car go forward
        """
        print('the car is in forward mode')
        self.motor_left.forward()
        self.motor_right.forward()
        self.action = 'z'
    def backward(self):
        """
        This method makes the car go backward
        """
        print('the car is in backward mode')
        self.motor_left.backward()
        self.motor_right.backward()
        self.action = 'z'
    def stopCar(self):
        """
        This method stops the car
        """
        print('the car is stopped')
        self.motor_left.stopMotor()
        self.motor_right.stopMotor()
        self.action = 'z'
    def turnRight(self):
        """
        This method turns the car to right
        """
        print('the car turns to right')
        self.motor_right.stopMotor()
        self.motor_left.forward()
        self.action = 'z'
    def turnLetf(self):
        """
        This method turns the car to left
        """
        print('the car turns to left')
        self.motor_left.stopMotor()
        self.motor_right.forward()
        self.action = 'z'
    def slowDownCar(self):
        """
        This method slows down the car
        """
        print('the car is in slow down mode')
        self.motor_right.slowDownMotor()
        self.motor_left.slowDownMotor()
        self.action = 'z'
    def speedUpCar(self):
        """
        This method speeds up the car
        """
        print('the car is in slow up mode')
        self.motor_right.speedUpMotor()
        self.motor_left.speedUpMotor()
        self.action = 'z'
    def mediumUpCar(self):
        """
        This method makes the car's speed to medium
        """
        print('the car is in medium speed mode')
        self.motor_right.setToMediumSpeed()
        self.motor_left.setToMediumSpeed()
        self.action = 'z'
