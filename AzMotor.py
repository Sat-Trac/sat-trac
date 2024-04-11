import motor


class AzMotor(motor.Motor):

    def __init__(self, enable_pin, pulse_pin, direction_pin, steps_per_rotation=0, gear_ratio=0):
        super().__init__(enable_pin, pulse_pin, direction_pin, steps_per_rotation, gear_ratio)

    def go_to_azimith(self, angle):
        super().__turn_to_degree(angle, wrap=True)
