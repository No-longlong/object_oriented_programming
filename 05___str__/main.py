class User:
    def __init__(self, n, m, p):
        self.name = n
        self.email = m
        self.password = p

# 특수메소드 dunder(double underscore): 특정 상황에 자동으로 호출
# dunder str 메소드는 인스턴스(user1) 출력(print)시에 실행
    def __str__(self):
        return f'사용자: {self.name}, 이메일: {self.email}, 비밀번호: ******'

user1 = User("Young", "young@codeit.kr", "123456")

user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")



print(user1)
# __str__을 지정해주지 않으면 <__main__.User object at 0x01124k214>가 뜬다.
# 위에서 나타나는 User는 클래스를 나타냄. 오른쪽은 메모리 주소
print(user2)
