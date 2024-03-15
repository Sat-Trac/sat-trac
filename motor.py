from time import sleep
import RPi.GPIO as GPIO


class Motor:
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

    def step(self):
        GPIO.output(self.pulse_pin, GPIO.HIGH)
        sleep(self.DELAY)
        GPIO.output(self.pulse_pin, GPIO.LOW)
        sleep(self.DELAY)

    def turn_degrees(self, degrees_to_turn):
        if degrees_to_turn > 0:
            direction = self.FORWARD
        else:
            direction = self.REVERSE
        self.enable_motor()
        self.set_motor_direction(direction)
        for x in range(0, degrees_to_turn, self.motor_step_degrees):
            print(x)
            self.step()
        self.disable_motor()

    def enable_motor(self):
        GPIO.output(self.enable_pin, GPIO.LOW)

    def disable_motor(self):
        GPIO.output(self.enable_pin, GPIO.HIGH)

    def set_motor_direction(self, direction):
        GPIO.output(self.direction_pin, direction)
