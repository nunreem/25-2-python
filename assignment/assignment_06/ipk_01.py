import tkinter as tk

class Vehicle:
    def __init__(self,name):
        self.name=name
    def drive(self):
        #이따 다시 확인하자

#class Car(Vehicle):
    def drive(self):
        return (f"승용차{self.name}가 주행합니다.")
    
class Truck (Vehicle):
    def drive(self):
        return (f"트럭{self.name}가 화물을 싣고 주행합니다.")
    
car=Car("car1")
truck=Truck("truck1")

###tkinter ui 구성 부분 다시 읽기!!!! ㅈㅉ중요제발
