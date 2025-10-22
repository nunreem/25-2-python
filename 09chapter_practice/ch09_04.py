class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def raise_salary(self,amount):
        self.salary += amount
        print(f"{self.name}의 연봉이{self.salary}원 인상되었습니다.")

kim=Employee("kim",5000)
Lee=Employee("Lee",6000)

print(f"{kim.name}의 연봉은 {kim.salary}원 입니다")
print(f"{Lee.name}의 연봉은 {Lee.salary}원 입니디")

kim.raise_salary(2000)
Lee.raise_salary(1000)