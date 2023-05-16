# parent class
class Vehicle:
    wheels = 4
    fuelType = 'Unknown'
    doors = 'Unknown'
    drivetrain = 'Unknown'

    def info(self):
        msg = "\nNumber of wheels: {}\nFuel type: {}\nNumber of doors: {}\nDrivetrain type: {}".format(self.wheels,self.fuelType,self.doors,self.drivetrain)
        return msg

# child class 1
class Truck(Vehicle):
    wheels = 4
    fuelType = 'Diesel'
    doors = '4'
    drivetrain = '4WD'
    bed = True
    transmission = 'Manual'

    def info(self):
        msg = "\nNumber of wheels: {}\nFuel type: {}\nNumber of doors: {}\nDrivetrain type: {}\nEquipped with a bed: {}\nTransmission Type: {}".format(self.wheels,self.fuelType,self.doors,self.drivetrain,self.bed,self.transmission)
        return msg

# chlid class 2
class Sedan(Vehicle):
    wheels = 4
    fuleType = 'Gasoline'
    doors = '4'
    drivetrain = 'FWD'
    trunk = True
    sunroof = True

    def info(self):
        msg = "\nNumber of wheels: {}\nFuel type: {}\nNumber of doors: {}\nDrivetrain type: {}\nEquipped with a trunk: {}\nEquipped with a sunroof: {}".format(self.wheels,self.fuelType,self.doors,self.drivetrain,self.trunk,self.sunroof)
        return msg


truck = Truck()
print(truck.info())

sedan = Sedan()
print(sedan.info())


