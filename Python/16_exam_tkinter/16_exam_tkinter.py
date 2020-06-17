import RPi.GPIO as GPIO
import time

from tkinter import *

# object
class DCMotor:
    def __init__(self, pPin, nPin, enPin):
        self.pPin = pPin
        self.nPin = nPin
        self.enPin = enPin
        
        GPIO.setup(pPin, GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(nPin, GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(enPin, GPIO.OUT, initial = GPIO.LOW)
    
    def turnPWMOn(self):
        self.pwm = GPIO.PWM(self.enPin, 100)
        self.pwm.start(0)
    
    def clockWise(self):
        GPIO.output(self.pPin, GPIO.HIGH)
        GPIO.output(self.nPin, GPIO.LOW)
        GPIO.output(self.enPin, GPIO.HIGH)
    
    def counterClockWise(self):
        GPIO.output(self.pPin, GPIO.LOW)
        GPIO.output(self.nPin, GPIO.HIGH)
        GPIO.output(self.enPin, GPIO.HIGH)
    
    def stop(self):
        GPIO.output(self.pPin, GPIO.HIGH)
        GPIO.output(self.nPin, GPIO.HIGH)
        GPIO.output(self.enPin, GPIO.HIGH)
    
    def _break(self):
        GPIO.output(self.pPin, GPIO.LOW)
        GPIO.output(self.nPin, GPIO.LOW)
        GPIO.output(self.enPin, GPIO.LOW)

#function
def sliderChanged(dutyCycle):
    motor.pwm.ChangeDutyCycle(int(dutyCycle))

# main
GPIO.setmode(GPIO.BOARD)
motor = DCMotor(15, 13, 11)
motor.turnPWMOn()

window = Tk()

frame = Frame(window)
frame.pack(side = 'top')

button1 = Button(frame,
                 text = "CW",
                 command = motor.clockWise)
button1.pack(side = 'left')

button2 = Button(frame,
                 text = "CCW",
                 command = motor.counterClockWise)
button2.pack(side = 'left')

button3 = Button(frame,
                 text = "STOP",
                 command = motor.stop)
button3.pack(side = 'left')

button4 = Button(frame,
                 text = "BREAK",
                 command = motor._break)
button4.pack(side = 'left')

slider = Scale(window,
               label = "LED0",
               orient = "h",
               from_ = 0, to_ = 100,
               command = sliderChanged)
slider.pack(side = 'top', fill = X)

window.mainloop()

motor._break()
GPIO.cleanup()
print("terminated")
