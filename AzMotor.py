from motor import Motor 


class AzMotor(Motor):

    def __init__(self, enable_pin, pulse_pin, direction_pin, steps_per_rotation=0, gear_ratio=0):
        super().__init__(enable_pin, pulse_pin, direction_pin, steps_per_rotation, gear_ratio)
        Motor.set_location(self,90)
        
    def go_to_azimuth(self, angle):
        
        Motor.turn_to_degrees(self, abs(angle-360), wrap=False)
