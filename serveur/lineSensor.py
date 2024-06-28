"""
This file contains class representing an Line sensor and its functions.  
Author: Abdessalam BOULAYAT & Imad AHDDAD
"""
import threading
import RPi.GPIO as GPIO

class LineSensor(threading.Thread):
    """
    A class representing a LineSensor connected to a car.

    Attributes:
    ----------
    **outGpioRight (int):** 
        the GPIO pin number to which the right LineSensor is connected  
    **outGpioLeft (int):** 
        the GPIO pin number to which the left LineSensor is connected  

    Methods:  
    **__init__(self, outGpioRight, outGpioLeft):** 
        Constructor for the LineSensor class  
    **setupLineSensor(self):** 
        Initializes the GPIO pins and sets up the LineSensors for use  
    **stop(self):** 
        Stop launched LineSensor thread  
    **run(self):** 
        Start LineSensor thread  
    """
    def __init__(self, outGpioRight,outGpioLeft):
        """
        Constructor for the LineSensor class should be called with two parameters specified above.  
        """
        super().__init__()
        self.stop_event = threading.Event()
        self.outGpioRight = outGpioRight
        self.outGpioLeft = outGpioLeft
        self.car = None
        self.setupLineSensor()
        print("lineSensor thread created")
    def setupLineSensor(self):
        """
        This method initializes the GPIO pins and sets up lineSensors for use
        """
        print("setup line sensor")
        GPIO.setup(self.outGpioLeft,GPIO.IN)
        GPIO.setup(self.outGpioRight,GPIO.IN)
    def stop(self):
        """
        This method stops lineSensor thread  
        """
        self.stop_event.set()
        print('\033[91m' + 'The line sensor is stopped' + '\033[0m')
    def run(self):
        """
        This is the first method that gets executed when a thread is started
        """
        print('\033[32m' + 'The line sensor thread is started now' + '\033[0m')
        # loop while the thread of lineSensor is started
        while not self.stop_event.is_set():
            # stop car if both left and right lineSensors detect the line
            if(GPIO.input(self.outGpioLeft) == True and GPIO.input(self.outGpioRight) == True):
                print("stop car")
                self.car.stopCar()
            # turn right if right lineSensor detects the line
            elif(GPIO.input(self.outGpioLeft) == False and GPIO.input(self.outGpioRight) == True):
                print("move right")
                self.car.turnRight()
            # turn left if left lineSensor detects the line
            elif(GPIO.input(self.outGpioLeft) == True and GPIO.input(self.outGpioRight) == False):
                print("move left")
                self.car.turnLetf()
            # forward if the line is not detected
            else:
                print("forward")
                self.car.forward()
