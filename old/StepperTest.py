# Connect GPIO pins as shown below) to the "-" input for each: ENA, PUL, and DIR
#
#
from time import sleep
import RPi.GPIO as GPIO
from motor import Motor
from APIClass import APIClass


# MOTOR 1
PUL1 = 16  # Stepper Drive Pulses
DIR1 = 20  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
ENA1 = 21  # Controller Enable Bit (High to Enable / LOW to Disable).

# MOTOR 2
PUL2 = 17  # Stepper Drive Pulses
DIR2 = 27  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
ENA2 = 22  # Controller Enable Bit (High to Enable / LOW to Disable).


GPIO.setmode(GPIO.BCM)

motor1 = Motor(ENA1, PUL1, DIR1, 6400, 1)  #Changed ratio to 1 for trial
motor2 = Motor(ENA2, PUL2, DIR2, 6400, 1)
motor1.turn_degrees(-10)
motor2.turn_degrees(-10)
motor1.turn_degrees(10)
motor2.turn_degrees(10)
motor1.turn_to_degrees(9)
motor2.turn_to_degrees(9)
motor1.turn_to_degrees(18)
motor2.turn_to_degrees(18)
motor1.turn_to_degrees(-18)
motor1.turn_to_degrees(-18)
sleep(1)
elevation_motor = Motor(ENA1, PUL1, DIR1, 6400, 1)  #Changed ratio to 1 for trial
azimuth_motor = Motor(ENA2, PUL2, DIR2, 6400, 1)

info = APIClass()
while(True):
    elv = info.getNextInfo()[0]
    azi = info.getNextInfo()[1]
    
    elevation_motor.turn_to_degrees(elv)
    sleep(0.5)
    azimuth_motor.turn_to_degrees(azi)
    sleep(0.5)

GPIO.cleanup()
print('Cycling Completed')
#
