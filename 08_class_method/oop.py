def add_print_to(original):
    def wrapper():
        print('함수 시작')
        original()
        print('함수 끝')
    return wrapper

@add_print_to
def print_hello():
    print('안녕하세요')

class User:
    count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        User.count += 1

    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다!")

    def __str__(self):
        return f'사용자: {self.name}, 이메일: {self.email}, 비밀번호: ******'

    @classmethod # 데코레이터
    def number_of_users(cls): # 클래스 메소드의 첫번째 파라미터 이름은 cls로 명명해야 한다.
                              # cls.count == User.count 가 성립된다.
        print(f'총 유저 수는: {cls.count}입니다.')

user1 = User("강", 'yo@naver.com', '123')
user2 = User("이", 'lee@naver.com', '12321')
user1 = User("박", 'park222@naver.com', '12345')

# 인스턴스 메소드는 user1을 첫번째 파라미터로 보내지만
# 클래스 메소드는 앞에 나온 User이나 user1이라는 클래스를 보낸다. (클래스 메소드 데코레이터)
User.number_of_users()
user1.number_of_users()