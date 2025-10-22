class Student:
    def __init__(self,name):
        self.name=name
        self.score=[] #score는 빈 리스트를 사용한다고 정의

    def add_score(self,score):
        self.score.append(score) 
        print(f"{self.name}의 성적이 추가되었습니다.")  

    def cal_avg(self):
        if not self.score:
            return 0
        return sum(self.score)/len(self.score) #이때 self.score은 리스트
    

#학생 인스턴스 생성
stu=Student("kim")

stu.add_score(90)
stu.add_score(85)
stu.add_score(70)

average=stu.cal_avg()
print(f"{stu.name}의 평균 성적은 {average:.2f}")