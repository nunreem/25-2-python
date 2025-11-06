class Car:
    def __init__(self, speed=0,gear=1,color="white"):
        self.__speed=speed
        self.__gear=gear
        self.__color=color

    def setSpeed(self,speed):
        self.__speed=speed
    
    def setGear(self,gear):
        self.__gear=gear
    
    def setColor(self,color):
        self.__color=color

    def __str__(self):
        return f"속도:{self.__speed}\n기어{self.__gear}\n색상{self.__color}"
    
mycar=Car()
mycar.setColor("red")
mycar.setGear(3)
mycar.setSpeed(100)

print(mycar)
