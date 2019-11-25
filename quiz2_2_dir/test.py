from app.vehicle import Vehicle, Airplane, TrainCar

bumper_car = Vehicle("400 lbs", "5 mph")
print(bumper_car.weight)

cessna = Airplane(max_altitude="15,000 ft", max_speed="130 mph")
print(isinstance(cessna, Airplane))
# prints True
print(isinstance(cessna, Vehicle))
# prints True
print(cessna.max_speed)
# prints "130 mph"

amtrak = TrainCar()
print(amtrak.weight)
# prints "65 tons"

git .amtrak.line = "blue"
print(amtrak.line)