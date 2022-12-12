import cv2
import numpy as np
from tensorflow import keras
from dc_motor import motor_operation
#from dc_motor_2 import motor_operation
from actuator import actuator_operation
import RPi.GPIO as GPIO          
from time import sleep

# ~ ########## Setting the first motor ##########
Motor1A = 24
Motor1B = 23
Motor1E = 25
temp1_1 = 1

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.LOW)
pwm1 = GPIO.PWM(Motor1E,1000)
pwm1.start(25)

# ~ ########## Setting the second motor ##########
Motor2A = 2
Motor2B = 3
Motor2E = 4
temp1_2 = 1

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.LOW)
pwm2 = GPIO.PWM(Motor2E,1000)
pwm2.start(25)

# # ~ ########## Setting the third motor ##########
# Motor3A = 2
# Motor3B = 3
# Motor3E = 4
# temp1_3 = 1

# GPIO.setup(Motor3A,GPIO.OUT)
# GPIO.setup(Motor3B,GPIO.OUT)
# GPIO.setup(Motor3E,GPIO.OUT)

# GPIO.output(Motor3A,GPIO.LOW)
# GPIO.output(Motor3B,GPIO.LOW)
# pwm3 = GPIO.PWM(Motor3E,1000)
# pwm3.start(25)

# # ~ ########## Setting the second motor ##########
# Motor4A = 2
# Motor4B = 3
# Motor4E = 4
# temp1_4 = 1

# GPIO.setup(Motor4A,GPIO.OUT)
# GPIO.setup(Motor4B,GPIO.OUT)
# GPIO.setup(Motor4E,GPIO.OUT)

# GPIO.output(Motor4A,GPIO.LOW)
# GPIO.output(Motor4B,GPIO.LOW)
# pwm4 = GPIO.PWM(Motor4E,1000)
# pwm4.start(25)

####### Setting linear actuator #####
forward = 16
backward = 26

GPIO.setup(forward,GPIO.OUT)
GPIO.setup(backward,GPIO.OUT)

########## Computer Vision Model ##########
model = keras.models.load_model('BTP_CV_Resnet.h5')

img_height, img_width = 224, 224
dimensions = (img_height, img_width)

video_capture = cv2.VideoCapture(0)
count = 30
frame_width = int(video_capture.get(3))
frame_height = int(video_capture.get(4))
frame_size = (frame_width , frame_height)
writer = cv2.VideoWriter("test_video_output.avi", cv2.VideoWriter_fourcc(*('MJPG')), 10 , frame_size)


########### Loop ############
while True:  
    ret, frame = video_capture.read()  # Read in the frame
    #if (ret == True):  
    # video_capture.set(cv2.CAP_PROP_POS_FRAMES, count)   # i.e. at 30 fps, this advances one second        
    image = cv2.resize(frame, dimensions)   # resize image        
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)    # change color channels form bgr to rgb        
    image = (image/255).astype(np.float16)    # normalise data
    image = image.reshape(1, image.shape[0], image.shape[1], image.shape[2])

    a = model.predict(image)
    output = frame.copy()
    ##### Motor Starts ######
    x = 'r'
    motor_operation(x, Motor1A, Motor1B, pwm1, temp1_1, Motor2A, Motor2B, pwm2, temp1_2)
    #motor_operation(x, Motor1A, Motor1B, pwm1, temp1_1, Motor2A, Motor2B, pwm2, temp1_2, Motor3A, Motor3B, pwm3, temp1_3, Motor4A, Motor4B, pwm4, temp1_4)
    x = 'f'
    motor_operation(x, Motor1A, Motor1B, pwm1, temp1_1, Motor2A, Motor2B, pwm2, temp1_2)
    #motor_operation(x, Motor1A, Motor1B, pwm1, temp1_1, Motor2A, Motor2B, pwm2, temp1_2, Motor3A, Motor3B, pwm3, temp1_3, Motor4A, Motor4B, pwm4, temp1_4)


    if a<0.5:
        # print("Cotton Plant")
        text = "Cotton Plant"
        cv2.putText(output, text, (35, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.25, (0, 0, 255), 5)
        x = 'm'
        motor_operation(x, Motor1A, Motor1B, pwm1, temp1_1, Motor2A, Motor2B, pwm2, temp1_2)
        #motor_operation(x, Motor1A, Motor1B, pwm1, temp1_1, Motor2A, Motor2B, pwm2, temp1_2, Motor3A, Motor3B, pwm3, temp1_3, Motor4A, Motor4B, pwm4, temp1_4)

        
    else:
        # print("Non Cotton Plant")
        text = "Non Cotton Plant"
        cv2.putText(output, text, (35, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.25, (0, 0, 255), 5)
        x = 's'
        motor_operation(x, Motor1A, Motor1B, pwm1, temp1_1, Motor2A, Motor2B, pwm2, temp1_2)
        #motor_operation(x, Motor1A, Motor1B, pwm1, temp1_1, Motor2A, Motor2B, pwm2, temp1_2, Motor3A, Motor3B, pwm3, temp1_3, Motor4A, Motor4B, pwm4, temp1_4)
        actuator_operation(forward, backward)

    writer.write(output)    
    cv2.imshow('Video Output', output)   # Display the frame

    if cv2.waitKey(1) == ord('q'):
        GPIO.cleanup()
        print("GPIO Clean up")
        break

# Stop filming
video_capture.release()
writer.release()

# Close down OpenCV
cv2.destroyAllWindows()
