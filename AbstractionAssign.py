from abc import ABC, abstractmethod

class house(ABC):
    def mortgage(self, amount):
        print("Your mortgage amount is: ",amount)
#This function is telling us to pass in an argument, but we won't tell you
#how or what kind of data it will be.
    def payment(self, amount):
        pass


class CreditCardPayment(house):
#here we've defined how to implement payment function from its parent mortgage class.
    def payment(self, amount):
        print("Your purchase amount of {} exceeded your $1000 limit ".format(amount))


obj = CreditCardPayment()
obj.mortgage("$2000")
obj.payment("$1500")
