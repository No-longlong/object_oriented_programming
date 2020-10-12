class User:
    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다.")

    def login(self, my_email, my_password):
        if (self.email == my_email and self.password == my_password):
            print("로그인 성공")
        else:
            print("로그인 실패")

user1 = User()

user1.name = "김객체"
user1.email = "oop@gmail.com"
user1.password = "oop1234"

user1.say_hello()
user1.login("oop@gmail.com", "oop1234")