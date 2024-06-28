"""
This file contains class representing a detector Thread and its behavior.

Author: AL FAIZ ASSIA
"""
import threading
import RPi.GPIO as GPIO
from time import sleep
from time import time
import random


class DetectorEmpty(threading.Thread):
    """
    A class that represents a distance detector using an ultrasound sensor. The detector measures the distance between
    an object and the sensor, and triggers certain actions based on that distance, such as turning on an LED or
    controlling the movement of a car.

    Attributes:
    ----------
    **stop_event (threading.Event):** 
        An event object used to signal the detector thread to stop  
    **trigGpio (int):** 
         The GPIO pin number for the trigger pin of the ultrasound sensor  
    **echoGpio (int):** 
        The GPIO pin number for the echo pin of the ultrasound sensor  
    **car (Car):** 
         A reference to the Car object that the detector controls  

    Methods:
    -------
    __init__(self, trigGpio, echoGpio): 
        Initializes a new instance of the Detector class  
    run(): 
        This is the first method that gets executed when a thread is started. It runs a continuous loop that measures the distance between the sensor and an object, and triggers certain actions based on that distance.  
    stop(): 
        Stops the detector thread.  
    setupDetector(): 
        Initializes the GPIO pins and sets up the detector for use.  
    is_even(number): 
        Tests if a given number is even or not.  

    """
    def __init__(self, trigGpio, echoGpio):
        """
        Initializes a new instance of the Detector class with the specified trigger and echo GPIO pins.

        Args:  
        trigGpio (int):
            The GPIO pin number for the trigger pin of the ultrasound sensor
        echoGpio (int):
            The GPIO pin number for the echo pin of the ultrasound sensor
        """
        super().__init__()
        self.stop_event = threading.Event()
        self.trigGpio = trigGpio
        self.echoGpio = echoGpio
        self.car = None
        self.setupDetector()
        print("detector thread created")

    def run(self):
        """
        This is the first method that gets executed when a thread is started
        """
        print('\033[32m' + 'The detector thrad is started now' + '\033[0m')
        while not self.stop_event.is_set():
            # We take it every 1 second
            sleep(1)
            GPIO.output(self.trigGpio, True)
            sleep(0.00001)
            GPIO.output(self.trigGpio, False)
            # Emission of ultrasound
            while GPIO.input(self.echoGpio)==0:
                debutImpulsion = time()
            # Return of the Echo
            while GPIO.input(self.echoGpio)==1:
                finImpulsion = time()
            # calculation of the distance knowing that the speed of sound = 340 m/s
            distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)
            print ("La distance est de : ",distance," cm")
            # if the distance is greater than 5 cm the car turns randomly to left or to right
            if(distance > 5):
                self.car.led.turnOnLed()
                # the car reacts only if it is not stopped
                if(self.car.motorDirection != 0):
                    random_integer = random.randint(0, 10)
                    # the car turns left or right randomly
                    if(self.is_even(random_integer)):
                        self.car.turnRight()
                    else:
                        self.car.turnLetf()
            # if the distance is less than 5cm the car continues its behavior
            else:
                self.car.led.turnOffLed()
                if(self.car.motorDirection == 1):
                    self.car.forward()
                elif(self.car.motorDirection == -1):
                    self.car.backward()
                elif(self.car.motorDirection == 2):
                    self.car.turnRight()
                elif(self.car.motorDirection == 3):
                    self.car.turnLetf()
                else:
                    self.car.stopCar()                

    def stop(self):
        """
        this methods stops the thread
        """        
        self.stop_event.set()
        print('\033[91m' + 'The detector is stopped' + '\033[0m')

    def setupDetector(self):
        """
        This method initializes the GPIO pins and sets up the detector for use
        """  
        GPIO.setup(self.trigGpio,GPIO.OUT)
        GPIO.setup(self.echoGpio,GPIO.IN)
        GPIO.output(self.trigGpio, False)
    
    def is_even(self, number):
        """
        this method tests if a given number is even or not

        Args:
            number (int): an integer number 

        Returns:
            bool: if number is even it returns True , if not it returns False 
        """        
        if number % 2 == 0:
            return True
        else:
            return False


        