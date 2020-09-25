class User:
    def __init__(self, n, m, p):
        self.name = n
        self.email = m
        self.password = p

    def __str__(self): # 인스턴스 출력(print)시에 실행
        return f'사용자: {self.name}, 이메일: {self.email}, 비밀번호: ******'

user1 = User("Young", "young@codeit.kr", "123456")

user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")



print(user1)
print(user2)
