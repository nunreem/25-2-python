class Animal:
    def __init__(self,name=""):
        self.name=name
    def eat(self):
        print("동물이 먹고 있습니다.")

class Dog(Animal): #상속할때 괄호 안에 부모클래스 이름 작성
    def __init__(self):
        super().__init__() #부모클래스 메소드 호출
    def eat(self):
        super().eat()
        print("강아지가 먹고 있습니다.")

d=Dog()
d.eat()