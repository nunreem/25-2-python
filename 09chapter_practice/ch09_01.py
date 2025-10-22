class Dog:
    def __init__(self,name, age):
        self.name = name #인스턴스 변수
        self.age = age
       
    def bark(self):
        print(f"{self.name}가 짖고 있습니다")

    def info(self):
        print(f"이름:{self.name}, 나이:{self.age}")

    

dog1 = Dog("바둑이",3)
dog2= Dog("멍멍이",3)

dog1.bark()
dog2.bark()

dog1.info()
dog2.info()