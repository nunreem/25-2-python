#is-a>>>상속

class Animal:
    def speak(self):
        print("동물이 소리를 낸다")

class Dog(Animal):
    def speak(self):
        print("멍멍")

dog=Dog()
dog.speak() 