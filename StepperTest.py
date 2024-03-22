# Connect GPIO pins as shown below) to the "-" input for each: ENA, PUL, and DIR
#
#
from time import sleep
import RPi.GPIO as GPIO
from motor import Motor


# MOTOR 2
PUL = 16  # Stepper Drive Pulses
DIR = 20  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
ENA = 21  # Controller Enable Bit (High to Enable / LOW to Disable).

motor = Motor(ENA, PUL, DIR, 1.8, 1)  #Changed ratio to 1 for trial
sleep(10)



# MOTOR 1
#PUL = 17  # Stepper Drive Pulses
#DIR = 27  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
#ENA = 22  # Controller Enable Bit (High to Enable / LOW to Disable).




GPIO.setmode(GPIO.BCM)


GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

print('PUL = GPIO 17 - RPi 3B-Pin #11')
print('DIR = GPIO 27 - RPi 3B-Pin #13')
print('ENA = GPIO 22 - RPi 3B-Pin #15')

print('Initialization Completed')
#
# Could have usesd only one DURATION constant but chose two. This gives play options.
durationFwd = 6400 # This is the duration of the motor spinning. used for forward direction
durationBwd = 6400 # This is the duration of the motor spinning. used for reverse direction
print('Duration Fwd set to ' + str(durationFwd))
print('Duration Bwd set to ' + str(durationBwd))
#
delay = 0.0001 # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
print('Speed set to ' + str(delay))
#
cycles = 1 # This is the number of cycles to be run once program is started.
cyclecount = 0 # This is the iteration of cycles to be run once program is started.
print('number of Cycles to Run set to ' + str(cycles))
#
#
def forward():
    GPIO.output(ENA, GPIO.LOW)
    print('ENA set to HIGH - Controller Enabled')
    #
    sleep(.5) # pause due to a possible change direction
    GPIO.output(DIR, GPIO.LOW)
    print('DIR set to LOW - Moving Forward at ' + str(delay))
    print('Controller PUL being driven.')
    for x in range(durationFwd): 
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)
    GPIO.output(ENA, GPIO.HIGH)
    print('ENA set to LOW - Controller Disabled')
    sleep(.5) # pause for possible change direction
    return
#
#
def reverse():
    GPIO.output(ENA, GPIO.LOW)
    print('ENA set to HIGH - Controller Enabled')
    #
    sleep(.5) # pause due to a possible change direction
    GPIO.output(DIR, GPIO.HIGH)
    print('DIR set to HIGH - Moving Backward at ' + str(delay))
    print('Controller PUL being driven.')
    #
    for y in range(durationBwd):
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)
    GPIO.output(ENA, GPIO.HIGH)
    print('ENA set to LOW - Controller Disabled')
    sleep(.5) # pause for possible change direction
    return

while cyclecount < cycles:
    forward()
    reverse()
    cyclecount = (cyclecount + 1)
    print('Number of cycles completed: ' + str(cyclecount))
    print('Number of cycles remaining: ' + str(cycles - cyclecount))
#
GPIO.cleanup()
print('Cycling Completed')
#
