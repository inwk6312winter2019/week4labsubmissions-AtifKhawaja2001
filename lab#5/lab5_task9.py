class Vehicle:
	pass
class LandVehicle(Vehicle):
	pass
class TrackedVehicle(LandVehicle):
	pass

for class1 in [Vehicle, LandVehicle, TrackedVehicle]:
	for class2 in [Vehicle, LandVehicle, TrackedVehicle]:
		print(issubclass(class1,class2),end='\t')
print()
