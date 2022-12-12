import RPi.GPIO as GPIO  
import time

def actuator_operation(forward, backward):
	GPIO.output(forward,GPIO.LOW)
	GPIO.output(backward,GPIO.HIGH)
	time.sleep(6)

	#deactivate both relays to brake
	GPIO.output(forward,GPIO.HIGH)
	GPIO.output(backward,GPIO.HIGH)
	time.sleep(1)

	#activate relay in other direction
	GPIO.output(forward,GPIO.HIGH)
	GPIO.output(backward,GPIO.LOW)
	time.sleep(5)

	#deactivate both relays
	GPIO.output(forward,GPIO.HIGH)
	GPIO.output(backward,GPIO.HIGH)
	time.sleep(1)
