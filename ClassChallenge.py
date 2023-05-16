# parent class
class Vehicle:
    noOfCylinders = ''
    noOfWheels = 4
    fuelType = ''
    drivetrain = ''
    typeTires = ''


# child class
class Truck(Vehicle):
    def __init__(noOfCylinders, noOfWheels, fuelType, drivetrain, typeTires):
        self.noOfCylinders = 8
        self.noOfWheels = 4
        self.fuelType = 'Gasoline'
        self.drivetrain = '4WD'
        self.typeTires = 'All-Terrain'

    def Info(self):
        msg = "\nNumber of cylidners: {}\nNumber of wheels: {}\nFuel Type: {}\nDrivetrain: {}\nTire Type: {}".format(self.noOfCylidners,self.noOfWheels,self.fuelType,self.drivetrain,self.typeTire)
        return msg












if __name__ == "__main__":
    truck = Truck()
    print(truck.Info)
    
