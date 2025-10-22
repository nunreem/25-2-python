class Dog:
    def __init__(self,name, age, trick):
        self.name = name #인스턴스 변수
        self.age = age
        self.trick = trick
       
    def bark(self):
        print(f"{self.name}가 짖고 있습니다")

    def info(self):
        print(f"이름:{self.name}, 나이:{self.age}")

    def show_tricks(self):
        print(f"{self.name}의 장기는 {self.trick}입니다.")


dog1 = Dog("바둑이",3,["뒹굴기","달리기"])
dog2= Dog("멍멍이",3,["먹기"])

dog1.bark()
dog2.bark()

dog1.info()
dog2.info()

dog1.show_tricks()
dog2.show_tricks()