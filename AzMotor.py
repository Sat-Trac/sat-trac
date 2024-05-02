from Motor import Motor


class AzMotor(Motor):

    def __init__(self, enable_pin, pulse_pin, direction_pin, steps_per_rotation=0, gear_ratio=0):
        super().__init__(enable_pin, pulse_pin, direction_pin, steps_per_rotation, gear_ratio)

    def go_to_azimuth(self, angle):
        print(f"az go to {angle}")
        Motor.turn_to_degrees(self, angle)
