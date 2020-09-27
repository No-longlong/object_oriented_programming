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
    #
    @classmethod # 클래스 메소드 데코레이터를 통해서 클래스가 호출되도록 함.
    def number_of_users(cls): # 클래스 메소드의 첫번째 파라미터 이름은 cls로 명명해야 한다.
                              # cls.count == User.count 가 성립된다.
        print(f'총 유저 수는: {cls.count}입니다.')

    # 클래스 메소드가 아닌 인스턴스 메소드로도 동일한 기능을 할 수 있다.
    # def number_of_users(self):  # 다만, 인스턴스 변수를 쓰지 않으니(self.name 없음)
    #                             # 굳이 인스턴스 메소드를 만들 이유가 없기 때문에
    #                             # 클래스 변수를 사용하기 위해서는
    #                             # 클래스 메소드를 사용하는 편이 낫다고 본다.
    #     print(f"총 유저 수는: {User.count}입니다.")

# user1 = User("강", 'yo@naver.com', '123')
# user2 = User("이", 'lee@naver.com', '12321')
# user1 = User("박", 'park222@naver.com', '12345')

# 인스턴스 메소드는 user1을 첫번째 파라미터로 보내지만
# 클래스 메소드는 앞에 나온 User이나 user1이라는 클래스를 보낸다. (클래스 메소드 데코레이터)
# User.number_of_users(user1)
# user1.number_of_users()

# 인스턴스가 하나도 없을 때 써야 하는 경우도 클래스 메소드를 사용한다.
User.number_of_users()

# 인스턴스 변수, 클래스 변수를 모두 사용할 때에는 인스턴스 메소드를 쓰면 된다.
# 클래스 메소드를 통해서는 인스턴스 변수를 부를 수 없다.

# 클래스 메소드 사용: 인스턴스 변수 안쓰는 경우, 인스턴스 자체가 없는 경우
# 인스턴스 메소드: 위의 경우 제외하고 모두 사용