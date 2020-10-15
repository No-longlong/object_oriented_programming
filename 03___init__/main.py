class User:
    def __init__(self, n, m, p): # magic method, special method (특수 메소드; 특정 상황에 자동으로 호출되는 메소드)
        self.name = n
        self.email = m
        self.password = p
# 인스턴스가 생성될 때 자동으로 호출
# class를 호출하자마자, __init__이 실행되면서
# 받은 파라미터를 통해 인스턴스 변수를 만들어주는 행위를 한다.

user1 = User("Young", "young@codeit.kr", "123456")

user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User("Taeho", "taeho@codeit.kr", "123abc")

user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# 순서
# 1. User 인스턴스(user1) 생성
# 2. __init__ 메소드 자동 호출

# init 메소드가 인스턴스 생성과 인스턴스 변수 초깃값 호출을 한줄에 할 수 있도록 만듬



print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)
