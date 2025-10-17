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

mycar=Car()   
mycar.setGear(3)
mycar.setSpeed(100)

print(mycar)

print("속도:",mycar._Car__speed)
print("기어:",mycar._Car__gear)
print("색상:",mycar._Car__color)
