# 인스턴스 변수와 파라미터 변수가 동일한 것은 전혀 지장 없음
class User:
    def say_hello(self):
        print(f"안녕하세요 {self.name}입니다.")

    def check_name(self, name):
        return self.name == name

user1 = User()
user2 = User()

user1.name = "김모씨"
user1.email = "mossi@gmail.com"
user1.pw = "1234"

user2.name = '이모씨'
user2.email = 'leemo@gmail.com'
user2.pw = '5678'

print(user1.check_name('김모씨')) # True
print(user1.check_name('강모씨')) # False