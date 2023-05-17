# This class makes use of _protected for encapsulation
class protected1:
    def __init__(self):
        self._protectedVar = 0

x = protected1()
x.protectedVar = 10
print(x.protectedVar)

# This class makes use of __private for encapsulation
class protected2:
    def __init__(self):
        self.__privateVar = 15

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

y = protected2()
y.getPrivate()
y.setPrivate(12)
y.getPrivate()
