"""
This file contains class representing a motor and its behavior.
Author: Imad AHDDAD
"""
import RPi.GPIO as GPIO
class Motor:
    """
    A class representing a DC motor with GPIO control.

    Attributes
    ----------
    **enableGpio (int):** 
        The GPIO pin connected to the motor's enable pin  
    **input1Gpio (int):** 
        The GPIO pin connected to the motor's input 1 pin  
    **input2Gpio (int):**
        The GPIO pin connected to the motor's input 2 pin  
    **pwm (PWM object):**
        The PWM object controlling the motor's speed  

    Methods
    -------
    **__init__(self, enableGpio, input1Gpio, input2Gpio):** 
        Constructor for the Motor class  
    **setUpMotor():** 
        Initializes the GPIO pins and sets up the motor for use.  
    **startMotor():** 
        Starts the motor with a duty cycle of 50%.  
    **forward():** 
        Makes the motor go forward.  
    **backward():** 
        Makes the motor go backward.  
    **stopMotor():** 
        Stops the motor.  
    **slowDownMotor():** 
        Slows down the motor by decreasing the duty cycle to 50%.  
    **speedUpMotor():** 
        Speeds up the motor by increasing the duty cycle to 100%.  
    **setToMediumSpeed():** 
        Sets the motor's speed to medium by setting the duty cycle to 75%.  
    """
    def __init__(self, enableGpio, input1Gpio, input2Gpio):
        """
        Constructs for the Motor class.

        Args:
        **enableGpio (int):** 
            The GPIO pin connected to the motor's enable pin  
        **input1Gpio (int):** 
            The GPIO pin connected to the motor's input 1 pin  
        **input2Gpio (int):** 
            The GPIO pin connected to the motor's input 2 pin  
        """
        self.enableGpio = enableGpio
        self.input1Gpio = input1Gpio
        self.input2Gpio = input2Gpio
        self.setUpMotor()
        self.pwm = None
        self.startMotor()

    def setUpMotor(self):
        """
        This method initializes the GPIO pins and sets up the motor for use
        """  
        GPIO.setup(self.enableGpio,GPIO.OUT)
        GPIO.setup(self.input1Gpio,GPIO.OUT)
        GPIO.setup(self.input2Gpio,GPIO.OUT)
    
    def startMotor(self):
        """
        This method starts the motor
        """ 
        self.pwm=GPIO.PWM(self.enableGpio,1000)
        # Start PWM with required Duty Cycle
        self.pwm.start(self.enableGpio)
        self.pwm.ChangeDutyCycle(50)

    def forward(self):
        """
        This method makes the motor go forward
        """ 
        GPIO.output(self.input1Gpio,GPIO.LOW)
        GPIO.output(self.input2Gpio,GPIO.HIGH)
    def backward(self):
        """
        This method makes the motor go backward
        """ 
        GPIO.output(self.input1Gpio,GPIO.HIGH)
        GPIO.output(self.input2Gpio,GPIO.LOW)
    def stopMotor(self):
        """
        This method stops the motor
        """ 
        GPIO.output(self.input1Gpio,GPIO.LOW)
        GPIO.output(self.input2Gpio,GPIO.LOW)
    def slowDownMotor(self):
        """
        This method slows down the motor
        """
        self.pwm.ChangeDutyCycle(50)
    def speedUpMotor(self):
        """
        This method speeds up the motor
        """
        self.pwm.ChangeDutyCycle(100)
    def setToMediumSpeed(self):
        """
        This method makes the motors's speed to medium
        """
        self.pwm.ChangeDutyCycle(75)
        