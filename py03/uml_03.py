class User:
    def __init__(self, user_id:int, name:str):
        self.__id=user_id
        self.__name=name

    def getTodo(self):
        return print("ToDo 객체를 변환하는 메서드")
    
    def write(self, text:str):
        print(f"{self.__name}이(가) 글 작성:{text}")

#자식클래스01
class Student(User):
    def study(self):
        print("학생 공부")

#자식클래스02
class Teacher(User):
    def teach(self):
        print("선생님 쉅")

student=Student(1,"김민수")
teacher=Teacher(2,"이수정")

student.write("열심히 공부해야지!")
student.study()

teacher.write("오늘은 상속 개념을 가르쳤습니다.")
teacher.teach()
