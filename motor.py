from time import sleep
import RPi.GPIO as GPIO
import math


# Need to generate inherited classes.

class Motor:
    current_position: float = 0
    FORWARD: int = GPIO.LOW
    REVERSE: int = GPIO.HIGH

    DELAY: float = 0.001

    def __init__(self, enable_pin, pulse_pin, direction_pin, steps_per_rotation=0, gear_ratio=0):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pulse_pin, GPIO.OUT)
        GPIO.setup(direction_pin, GPIO.OUT)
        GPIO.setup(enable_pin, GPIO.OUT)
        self.enable_pin = enable_pin
        self.pulse_pin = pulse_pin
        self.direction_pin = direction_pin
        self.steps_per_rotation = steps_per_rotation
        self.gear_ratio = gear_ratio
        self.current_position = 0
        self.pulses_per_degree = 360 / steps_per_rotation * gear_ratio
        self.current_direction = self.FORWARD

    def step(self):
        GPIO.output(self.pulse_pin, GPIO.HIGH)
        sleep(self.DELAY)
        if self.current_direction == Motor.FORWARD:
            self.current_position += self.pulses_per_degree
        else:
            self.current_position -= self.pulses_per_degree
        self.current_position %= 360
        GPIO.output(self.pulse_pin, GPIO.LOW)
        sleep(self.DELAY)

    def turn_degrees(self, degrees_to_turn):

        if degrees_to_turn <= 0:
            direction = self.FORWARD
        else:
            direction = self.REVERSE
        self.enable_motor()
        self.set_motor_direction(direction)
        pulses_to_move = int(round(math.fabs(degrees_to_turn / self.pulses_per_degree)))
        for x in range(pulses_to_move):
            self.step()
        self.disable_motor()


    def turn_to_degrees(self, target_angle, wrap=False):
        print(self.current_position)
        if not wrap:
            degrees_to_travel = self.current_position - target_angle
        else:
            degree_distance = self.current_position - target_angle;
            if degree_distance <= 180:
                degrees_to_travel = self.current_position - target_angle
            else:
                degrees_to_travel = self.current_position - (math.ceil(self.current_position/360) * 360) - target_angle
        print(degrees_to_travel)

        self.turn_degrees(degrees_to_travel)
        print(self.current_position)

    def enable_motor(self):
        GPIO.output(self.enable_pin, GPIO.LOW)

    def disable_motor(self):
        GPIO.output(self.enable_pin, GPIO.HIGH)

    def set_motor_direction(self, direction):
        self.current_direction = direction
        GPIO.output(self.direction_pin, direction)

    def set_zero(self):
        self.current_position = 0

    def goto_zero(self):
        self.turn_to_degrees(0)
