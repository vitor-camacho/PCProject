# These are the libraries to import into the raspberry pi to run the motor
from machine import Pin, PWM
from L298N_motor import L298N
import time
#from ulab import numpy as np

# Required initialization of the pump
ENA = PWM(Pin(0))        
IN1 = Pin(1, Pin.OUT)         
IN2 = Pin(2, Pin.OUT)

motor1 = L298N(ENA, IN1, IN2)     #create a motor1 object, which will be used to call the motor on/off

x = np.linspace(40000,65534,200)
#motor1.setSpeed(2000)            #set the speed of motor1. Speed value varies from 25000 to 65534


#while True:

    
for i in x:
    motor1.setSpeed(int(i)) 
    motor1.forward()      #run motor1 forward
    print(i)
    time.sleep(0.05)         #wait for 5 seconds


time.sleep(3)
motor1.stop()
