import RPi.GPIO as GPIO          
import time
#from camera_capture import *


GPIO.getmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
sleeptime=1

# ~ ########## Setting all the motor ##########
#1: Front Right, 2: Front Left, 3:Back RIght, 4: Back Left, 5: Cutting Motor 1, 6: Cutting Motor 2
Motor1A = 12
Motor1B = 13
Motor1Enable = 11
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1Enable,GPIO.OUT)

Motor2A = 10
Motor2B = 8
Motor2Enable = 7
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2Enable,GPIO.OUT)


Motor3A = 31
Motor3B = 29
Motor3Enable = 32
GPIO.setup(Motor3A,GPIO.OUT)
GPIO.setup(Motor3B,GPIO.OUT)
GPIO.setup(Motor3Enable,GPIO.OUT)


Motor4A = 36
Motor4B = 35
Motor4Enable = 33
GPIO.setup(Motor4A,GPIO.OUT)
GPIO.setup(Motor4B,GPIO.OUT)
GPIO.setup(Motor4Enable,GPIO.OUT)

Motor5A = 21
Motor5B = 22
GPIO.setup(Motor5A,GPIO.OUT)
GPIO.setup(Motor5B,GPIO.OUT)

# Motor6A = 16
# Motor6B = 18
# GPIO.setup(Motor6A,GPIO.OUT)
# GPIO.setup(Motor6B,GPIO.OUT)

# Set up PWM frequency and start PWM
pwm1 = GPIO.PWM(Motor1Enable, 100)
pwm2 = GPIO.PWM(Motor2Enable, 100)
pwm3 = GPIO.PWM(Motor3Enable, 100)
pwm4 = GPIO.PWM(Motor4Enable, 100)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)

############## Setting up linear actuator ############
forward_channel = 16
backward_channel = 19
GPIO.setup(forward_channel,GPIO.OUT)
GPIO.setup(backward_channel,GPIO.OUT)

############## Operation Functions ############
def forward(x, speed):
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor3A,GPIO.HIGH)
    GPIO.output(Motor4A,GPIO.HIGH)
        
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(speed)
    pwm3.ChangeDutyCycle(speed)
    pwm4.ChangeDutyCycle(speed)
        

    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor3A,GPIO.LOW)
    GPIO.output(Motor4A,GPIO.LOW)
        
    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)
    pwm3.ChangeDutyCycle(0)
    pwm4.ChangeDutyCycle(0)

########## Reverse ###########	
def reverse(x, speed):
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor3B,GPIO.HIGH)
    GPIO.output(Motor4B,GPIO.HIGH)
        
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(speed)
    pwm3.ChangeDutyCycle(speed)
    pwm4.ChangeDutyCycle(speed)
        
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor3B,GPIO.LOW)
    GPIO.output(Motor4B,GPIO.LOW)

    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)
    pwm3.ChangeDutyCycle(0)
    pwm4.ChangeDutyCycle(0)
    
######## Left Turn #########
def left_turn(x, speed):
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor3A,GPIO.HIGH)
    GPIO.output(Motor4B,GPIO.HIGH)
        
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(speed)
    pwm3.ChangeDutyCycle(speed)
    pwm4.ChangeDutyCycle(speed)

    print("Moving Left")
    time.sleep(x)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor3A,GPIO.LOW)
    GPIO.output(Motor4B,GPIO.LOW)

    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)
    pwm3.ChangeDutyCycle(0)
    pwm4.ChangeDutyCycle(0)

########## Right Turn ###########
def right_turn(x, speed):
    GPIO.output(Motor1A,GPIO.HIGH)    
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor3B,GPIO.HIGH)
    GPIO.output(Motor4A,GPIO.HIGH)

    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(speed)
    pwm3.ChangeDutyCycle(speed)
    pwm4.ChangeDutyCycle(speed)

    print("Moving Right")
    time.sleep(x)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor3B,GPIO.LOW)
    GPIO.output(Motor4A,GPIO.LOW)

    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)
    pwm3.ChangeDutyCycle(0)
    pwm4.ChangeDutyCycle(0)

def cutting():
    GPIO.output(Motor5A, GPIO.HIGH)
    GPIO.output(Motor5B, GPIO.LOW)
    #GPIO.output(Motor6B, GPIO.HIGH)
    print("Cutting")

def stop_cutting():
    GPIO.output(Motor5A, GPIO.LOW)
    #GPIO.output(Motor6B, GPIO.LOW)
    print("Stopped Cutting")

# def right_turn_curve(x, speed):
#     GPIO.output(Motor1A,GPIO.HIGH)    
#     GPIO.output(Motor2A,GPIO.HIGH)
#     GPIO.output(Motor3A,GPIO.HIGH)
#     GPIO.output(Motor4A,GPIO.HIGH)

#     pwm1.ChangeDutyCycle(speed)
#     pwm2.ChangeDutyCycle(0)
#     pwm3.ChangeDutyCycle(0)
#     pwm4.ChangeDutyCycle(speed)

#     print("Moving Right")
#     time.sleep(x)
#     GPIO.output(Motor1B,GPIO.LOW)
#     GPIO.output(Motor2B,GPIO.LOW)
#     GPIO.output(Motor3B,GPIO.LOW)
#     GPIO.output(Motor4B,GPIO.LOW)

#     pwm1.ChangeDutyCycle(0)
#     pwm2.ChangeDutyCycle(0)
#     pwm3.ChangeDutyCycle(0)
#     pwm4.ChangeDutyCycle(0)

def actuate():
    GPIO.output(forward_channel, GPIO.HIGH)
    GPIO.output(backward_channel, GPIO.LOW)
    print("actuate")  
def dactuate():
   GPIO.output(forward_channel, GPIO.LOW)
   GPIO.output(backward_channel, GPIO.HIGH)
   print("dactuate")

while (1):
    speed = 100
    reverse(5, speed)
    # actuate()
    # time.sleep(2)
    # dactuate()
    # time.sleep(2)
    # cutting()
    # time.sleep(5)
    # stop_cutting()
    #dactuate()
    #time.sleep(5)
    #right_turn(1.5, 100)
    #time.sleep(1)
    #left_turn(1)
    #actuate()
    #time.sleep(2)
    #dactuate()
    #time.sleep(10)
    #forward(2, speed)
    #time.sleep(1)
    #right_turn(5, 100)

        # Stop motors and clean up GPIO pins
    pwm1.stop()
    pwm2.stop()
    pwm3.stop()
    pwm4.stop()

    GPIO.cleanup()
    break


