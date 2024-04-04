from time import sleep
import RPi.GPIO as GPIO

# Need to 

class Motor:
    current_position = 0
    FORWARD = GPIO.LOW
    REVERSE = GPIO.HIGH
    DELAY = 0.001

    def __init__(self, enable_pin, pulse_pin, direction_pin, motor_step_degrees=0, gear_ratio=0):
        self.enable_pin = enable_pin
        self.pulse_pin = pulse_pin
        self.direction_pin = direction_pin;
        self.motor_step_degrees = motor_step_degrees
        self.gear_ratio = gear_ratio
        self.degrees = 0
        self.pulse_degrees = motor_step_degrees / gear_ratio
        self.turn_degrees(10)

    def step(self):
        GPIO.output(self.pulse_pin, GPIO.HIGH)
        sleep(self.DELAY)
        GPIO.output(self.pulse_pin, GPIO.LOW)
        sleep(self.DELAY)

    def turn_degrees(self, degrees_to_turn):

        #needs to update current position
        
        if degrees_to_turn > 0:
            direction = self.FORWARD
        else:
            direction = self.REVERSE
        self.enable_motor()
        self.set_motor_direction(direction)
        for x in [x * self.motor_step_degrees for x in range(0, degrees_to_turn)]:
            print(x)
            self.step()
        self.disable_motor()

    def turn_to_heading(self, target):
        # This should use current_position and turn_degrees to go to a specific angle
        # Make sure we don't exceed turning limits
        pass

    def enable_motor(self):
        GPIO.output(self.enable_pin, GPIO.LOW)

    def disable_motor(self):
        GPIO.output(self.enable_pin, GPIO.HIGH)

    def set_motor_direction(self, direction):
        GPIO.output(self.direction_pin, direction)

    def set_zero(self):
        current_position = 0
        pass

    def goto_zero(self):
        # move the moter from the current position to zero
        pass
