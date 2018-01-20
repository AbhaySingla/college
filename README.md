# PIR Sensor

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
The .stl files for them are in the [zip forler](https://github.com/AbhaySingla/college/blob/master/3d%20printing.zip).

## Start
- Testing the PIR sensor:
1.  Connect the sensor as shown in the schema
2.  Open the console
3.  Open a new python script
  ```Shell
      sudo nano pirtest.py
 ```
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
  ```Shell
     sudo chmod u+x pirtest.py
  ``` 
 6. Execute the script, to exit the script use Ctrl. + c 
 ```Shell
     python pirtest.py
 ```
 7. If test the sensor by moving infront of it, remember there is a 2 seconds delay in between two readings in the script provided above.
 
- Test the Camera.

