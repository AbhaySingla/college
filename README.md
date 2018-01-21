# PIR Sensor

## Index
1.  [Stuff you need](#stuff you need)

## Stuff you need (All the prices are from amazon.ca and may change by thime you see them):
- Raspberry Pi 3 with a case and a power-supply(I only worked on a pi3, but its only a simple python code so it should run on other models, but I am not sure of it)<br>
-- $79.99 + Tax
- PIR Sensor <br>
-- $8.99 + Tax for 1 sensor<br>
-- $12.99+ Tax for 3 sensors
- Camera Module<br>
-- $29.99+ Tax
- Female-Female jumper wire<br>
-- There are options from $6 for a 20 pack, you need only 3 wires for this project.
### Extras(This is just to load the libraries and code to the pi)
- HDMI Display
- KeyBoard
- Mouse

## Project Schema
![Alt text](https://github.com/AbhaySingla/college/blob/master/project%20Schema.jpeg)

## Sensor Housings
I used the case in the kit for the pi, and I 3D printed housings for the camera and sensor.
The .stl files for them are in the [zip forler](https://github.com/AbhaySingla/college/blob/master/3d%20printing.zip).<br>
This process might take you upto a day.

## Start (This whole process will take you upto 4 hours.)

#### Setting up RaspberryPI
1. Connect the display in the HDMI port, connect the keyboard and he mouse and also give the pi an eathernet connection.
2. On the first boot, with NOOBS installed on you sd card, you will be asked to install the OS.
3. Select the raspbian OS, and wait for it to install. This might take upto 15 mins.

#### Testing the PIR sensor:
1.  Connect the sensor as shown in the schema (VCC- pin2, GND- pin6, DigitalOutput- pin7)
2.  Open the console
3.  Open a new python script
    ```
    sudo nano pirtest.py

4. Write the following code in the the file:
  ```Shell
     import RPi.GPIO as GPIO                           
     import time
     
     GPIO.setmode(GPIO.BOARD)
     pir = 7
     GPIO.setup(pir, GPIO.IN)
     print ("Waiting for sensor to settle")
     time.sleep(2)
     print ("Detecting motion")
     while True:
         if GPIO.input(pir):
                 print ("Motion Detected!")
                 time.sleep(2)
         time.sleep(0.1)

 ```
 5. Make the scipt excecutable
    ```
    sudo chmod u+x pirtest.py
 
 6. Execute the script, to exit the script use Ctrl. + c 
    ```
    python pirtest.py

 7. If test the sensor by moving infront of it, remember there is a 2 seconds delay in between two readings in the script provided above.
 
#### Test the Camera.
 1. Enable the picamera.
    ```
    sudo raspi-config
 
 2. Select ```Enable camera``` and hit ```Enter```, then go to ```Finish``` and you'll be prompted to reboot.
 3. The ```python-picamera``` library is available in the Raspbian archives.<br> 
    Install with  apt:
    ```
    sudo apt-get update
    sudo apt-get install python-picamera
 (This is the only part where you need to wait and do nothing, it might take you upto 15 minutes.)
 
 4. Open a new python script
    ```
    sudo nano camratest.py
     
 5. Write the following code in the the file:
  ```Shell
     import picamera
     from time import sleep
     
     camera = picamera.PiCamera()
     camera.capture('image1.jpg')
     sleep(5)
     camera.capture('image2.jpg')
  ```
 6. Make the scipt excecutable
    ```
    sudo chmod u+x cameratest.py
  
 7. Execute the script 
    ```
    python cameratest.py
 
 8. This code will click two pictures, in an interval of 5 seconds, stored in the home directory by the names ```image1.jpg``` and ```image2.jpg```
 
#### Getting both the components together
 1. Now that we know, both of our PIR sensor and the camera module works as desired, we can start writing our code.
 2.  Open a new python script
     ```
     sudo nano pirandcamera.py
 
 3. Write the following code in the the file:
    ```Shell
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
            img = img+1
            time.sleep(10)
            camera.capture("testimg"+str(img)+".jpg")
            camera.stop_preview()
    
        time.sleep(0.1)   
    ```
 
 4. Make the scipt excecutable
    ```
    sudo chmod u+x pirandcamera.py
  
 5. Execute the script 
    ```
    python pirandcamera.py
 
 6. When you run this script, as soon as the sensor detectes motion, the camera will turn on for 10 seconds and a picture will be clicked. The pictures will be saved in the home directory.
 
 ## Unit Testing
 
 ## Production Testing
 

