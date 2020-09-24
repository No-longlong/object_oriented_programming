class User:
    def __init__(self, n, m, p):
        self.name = n
        self.email = m
        self.password = p
# class를 호출하자마자, __init__이 실행되면서
# 받은 파라미터를 통해 인스턴스 변수를 만들어주는 행위를 한다.

user1 = User("Young", "young@codeit.kr", "123456")

user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User("Taeho", "taeho@codeit.kr", "123abc")

user4 = User("Lisa", "lisa@codeit.kr", "abc123")



print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)