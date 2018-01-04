import RPi.GPIO as GPIO                           
import time
import picamera

GPIO.setmode(GPIO.BOARD)                          
pir = 7                                         
GPIO.setup(pir, GPIO.IN)                           
print ("Waiting for sensor to settle")
time.sleep(2)                                     
print ("Detecting motion")
img = 1
camera = picamera.PiCamera()
while True:
    if GPIO.input(pir):
        print ("Motion Detected!")
        
        camera.start_preview()
        camera.capture("testimg"+str(img)+".jpg")
        img = img+1
        time.sleep(10)
        camera.stop_preview()
    
    time.sleep(0.1)                                
