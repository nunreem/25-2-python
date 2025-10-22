class bankAccount:
    interest_rate=0.3 #예금 이율
    def __init__(self, name, number, balance):
        self.name=name
        self.number=number
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance+=amount
            print("인출 성공")

        else:
            print("잔액이 부족합니다")

user1=bankAccount("chung","11111111",10000)
print(f"초기 잔고: {user1.balance}")
user1.deposit(5000)
print(f"저축 후 잔고:{user1.balance}")
user1.withdraw(2000)
print(f"인출 후 잔고:{user1.balance}")
