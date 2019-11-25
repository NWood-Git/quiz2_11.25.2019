class Vehicle():
    def __init__(self, weight = None, max_speed = None):
        self.weight = weight
        self.max_speed = max_speed

class Airplane(Vehicle):
    def __init__(self, weight=None, max_speed=None, max_altitude=None, make=None):
        super().__init__(weight,max_speed)
        self.max_altitude = max_altitude
        self.make = make

class TrainCar(Vehicle):
    def __init__(self, weight="65 tons", max_speed="150 mph", line = None):
        super().__init__(weight,max_speed)
        self.line = line #or was thinking self.line = None and not have it on the line with the init


