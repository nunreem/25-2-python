#hasa에 맞춰 코드 수정해두기. 현재 적힌 코드는 is a 
#01. Dog is an Animal

class Animal:
    def move(self):
        print("동물이 움직입니다")
        
class Dog(Animal):
    def move(self):
        super().move()
        print("개가 달립니다")




#02. Student is a person

class Person:
    def speak(self):
        print("사람이 말을 합니다")

class Student(Person):
    def study(self):
        print("학생이 공부합니다.")

stu=Student()
stu.speak
stu.study




#3.Car is a Vehicle

class Vehicle:
    def drive(self):
        print("차량이 이동 중입니다")

class Car(Vehicle):
    def drive(self):
        super().drive()
        print("자동차가 도로를 달립니다")

car=Car()
car.drive()