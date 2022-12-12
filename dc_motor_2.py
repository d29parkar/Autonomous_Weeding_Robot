import RPi.GPIO as GPIO          
from time import sleep

def motor_operation(x, Motor1A, Motor1B, pwm1, temp1_1, Motor2A, Motor2B, pwm2, temp1_2, Motor3A, Motor3B, pwm3, temp1_3,
                    Motor4A, Motor4B, pwm4, temp1_4):
    if x=='r':
        print("run")
        if(temp1_1==1 and temp1_2==1 and temp1_3==1 and temp1_4==1):
            GPIO.output(Motor1A,GPIO.HIGH)
            GPIO.output(Motor1B,GPIO.LOW)
                 
            GPIO.output(Motor2A,GPIO.HIGH)
            GPIO.output(Motor2B,GPIO.LOW)
            
            GPIO.output(Motor3A,GPIO.HIGH)
            GPIO.output(Motor3B,GPIO.LOW)
            
            GPIO.output(Motor4A,GPIO.HIGH)
            GPIO.output(Motor4B,GPIO.LOW)
                 
            print("forward")
            x='z'
        else:
            GPIO.output(Motor1A,GPIO.LOW)
            GPIO.output(Motor1B,GPIO.HIGH)
                 
            GPIO.output(Motor2A,GPIO.LOW)
            GPIO.output(Motor2B,GPIO.HIGH)
            
            GPIO.output(Motor3A,GPIO.LOW)
            GPIO.output(Motor3B,GPIO.HIGH)
            
            GPIO.output(Motor4A,GPIO.LOW)
            GPIO.output(Motor4B,GPIO.HIGH)
                 
            print("backward")
            x='z'


    elif x=='s':
        print("stop")
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.LOW)
        
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.LOW)
        
        GPIO.output(Motor3A,GPIO.LOW)
        GPIO.output(Motor3B,GPIO.LOW)
        
        GPIO.output(Motor4A,GPIO.LOW)
        GPIO.output(Motor4B,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        
        GPIO.output(Motor3A,GPIO.HIGH)
        GPIO.output(Motor3B,GPIO.LOW)
        
        GPIO.output(Motor4A,GPIO.HIGH)
        GPIO.output(Motor4B,GPIO.LOW)
        temp1_1=1
        temp1_2=1
        temp1_3=1
        temp1_4=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        
        GPIO.output(Motor3A,GPIO.LOW)
        GPIO.output(Motor3B,GPIO.HIGH)
        
        GPIO.output(Motor4A,GPIO.LOW)
        GPIO.output(Motor4B,GPIO.HIGH)
        
        temp1_1=0
        temp1_2=0
        temp1_3=0
        temp1_4=0
        x='z'

    elif x=='l':
        print("low")
        pwm1.ChangeDutyCycle(25)
        pwm2.ChangeDutyCycle(25)
        pwm3.ChangeDutyCycle(25)
        pwm4.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        pwm1.ChangeDutyCycle(50)
        pwm2.ChangeDutyCycle(50)
        pwm3.ChangeDutyCycle(50)
        pwm4.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        pwm1.ChangeDutyCycle(75)
        pwm2.ChangeDutyCycle(75)
        pwm3.ChangeDutyCycle(75)
        pwm4.ChangeDutyCycle(75)
        x='z'

    elif x=='le':
        print("Turning left")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        
        GPIO.output(Motor3A,GPIO.HIGH)
        GPIO.output(Motor3B,GPIO.LOW)
        
        GPIO.output(Motor4A,GPIO.LOW)
        GPIO.output(Motor4B,GPIO.HIGH)       
        x='z'
        
    elif x=='ri':
        print("Turning right")
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        
        GPIO.output(Motor3A,GPIO.LOW)
        GPIO.output(Motor3B,GPIO.HIGH)
        
        GPIO.output(Motor4A,GPIO.HIGH)
        GPIO.output(Motor4B,GPIO.LOW)       
        x='z'       
    
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")