#This class is the parent class defining the main properties
class computer:
    CPU = ''
    RAM = ''
    Motherboard = ''
    Case = ''

#This class is a child class of 'computer', with some unique properties
class Desktop(computer):
    GPU = ''
    PowerSupply = ''

#This class is also a child class of 'computer', with some unique properties
class Laptop(computer):
    Battery = ''
    Screen = ''
