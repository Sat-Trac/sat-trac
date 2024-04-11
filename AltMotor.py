import motor


class AltMotor(motor.Motor):

    def __init__(self, enable_pin, pulse_pin, direction_pin, steps_per_rotation=0, gear_ratio=0):
        super().__init__(enable_pin, pulse_pin, direction_pin, steps_per_rotation, gear_ratio)

    def turn_to_alt(self, angle):
        super().__turn_to_degree(max(0, min(angle, 90)))

