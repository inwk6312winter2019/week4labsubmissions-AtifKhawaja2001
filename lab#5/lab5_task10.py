class Vehicle:
	pass
class LandVehicle(Vehicle):
	pass
class TrackedVehicle(LandVehicle):
	pass

vehicle = Vehicle()
landvehicle = LandVehicle()
trackedvehicle = TrackedVehicle()

for ob in [vehicle, landvehicle, trackedvehicle]:
	for cl in [Vehicle, LandVehicle, TrackedVehicle]:
		print(isinstance(ob,cl),end='\t')
print()
