from time import sleep
import RPi.GPIO as GPIO
import math


class Motor:
    
    current_position: float = 0
    DELAY: float = 0.002

    def __init__(self, enable_pin, pulse_pin, direction_pin, steps_per_rotation=0, gear_ratio=0):
        self.FORWARD: int = GPIO.HIGH
        self.REVERSE: int = GPIO.LOW
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
        self.degrees_per_pulse = 360 / (steps_per_rotation * gear_ratio)
        self.current_direction = self.FORWARD

    def step(self):
        GPIO.output(self.pulse_pin, GPIO.HIGH)
        sleep(self.DELAY)
        if self.current_direction == self.FORWARD:
            self.current_position += self.degrees_per_pulse
        else: 
            self.current_position -= self.degrees_per_pulse
        GPIO.output(self.pulse_pin, GPIO.LOW)
        sleep(self.DELAY)

    def step_with_delay(self, delay_time):
        GPIO.output(self.pulse_pin, GPIO.HIGH)
        sleep(delay_time)
        if self.current_direction == self.FORWARD:
            self.current_position += self.degrees_per_pulse
        else:
            self.current_position -= self.degrees_per_pulse
        GPIO.output(self.pulse_pin, GPIO.LOW)
        sleep(delay_time)

    def calc_delay(self, degrees):
        degrees = math.fabs(degrees)
        if degrees > 2:
            return self.DELAY
        else:
            return .5/(degrees / self.degrees_per_pulse)  # Allowing half second per motor - change .5 to 1 when threading?

    def turn_degrees(self, degrees_to_turn):
        if degrees_to_turn <= 0:
            direction = self.FORWARD
        else:
            direction = self.REVERSE
        self.enable_motor()
        self.set_motor_direction(direction)
        pulses_to_move = int(round(math.fabs(degrees_to_turn / self.degrees_per_pulse)))
        print(f"Beginning turn of {degrees_to_turn} : {pulses_to_move} pulses")
        for x in range(pulses_to_move):
            self.step_with_delay(self.calc_delay(degrees_to_turn))
        if self.current_position < 0:
                self.current_position += 360
        print("Completed turn")

    def turn_to_degrees(self, target_angle):

        degrees_to_travel = self.current_position - target_angle
        self.turn_degrees(degrees_to_travel)

    def enable_motor(self):
        GPIO.output(self.enable_pin, GPIO.LOW)

    def disable_motor(self):
        GPIO.output(self.enable_pin, GPIO.HIGH)

    def set_motor_direction(self, direction):
        self.current_direction = direction
        GPIO.output(self.direction_pin, direction)

    def set_location(self, position_degrees):
        self.current_position = position_degrees

    def set_zero(self):
        self.current_position = 0

    def goto_zero(self):
        self.turn_to_degrees(0)
