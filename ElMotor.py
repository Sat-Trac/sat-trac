from Motor import Motor


class ElMotor(Motor):

    def __init__(self, enable_pin, pulse_pin, direction_pin, steps_per_rotation=0, gear_ratio=0):
        super().__init__(enable_pin, pulse_pin, direction_pin, steps_per_rotation, gear_ratio)

    # Make sure  stays between 0 and 90 then turn to the required setting
    def go_to_elevation(self, angle):
        print(f"el go to {angle}")
        if angle > 90:
            angle = 90
        elif angle < 0:
            angle = 0
        Motor.turn_to_degrees(self, angle)
