from motor import Motor


class AltMotor(Motor):

    def __init__(self, enable_pin, pulse_pin, direction_pin, steps_per_rotation=0, gear_ratio=0):
        super().__init__(enable_pin, pulse_pin, direction_pin, steps_per_rotation, gear_ratio)
        Motor.set_location(self,90);

    def turn_to_altitude(self, angle):
        Motor.turn_to_degrees(self, max(-90, min(angle, 90)), wrap=False)

