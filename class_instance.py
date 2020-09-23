class User: # 클래스 이름 첫글자는 대문자
    pass

# 같은 클래스로 만든 유저이지만
# 같은 클래스여도 각각은 다른 유저 인스턴스이다.
user1 = User()
user2 = User()
user3 = User()

# '속성' 추가는 '변수' 와 비슷하다.
# 인스턴스가 개인적으로 갖고 있는 속성을 "인스턴스 변수" 라고 한다. ex.name, email, password

user1.name = "김대위"
user1.email = "captain@gmail.co.kr"
user1.password = "12345"

user2.name = "이소위"
user2.email = "sowe@gmail.co.kr"
user2.password = "123454321"

user3.name = "김태희"
user3.email = "taheegmail.co.kr"
user3.password = "1234500000"

# 인스턴스 변수 사용하기
print(user1.email)
print(user2.password)

# print(user1.age) 인스턴스 변수를 미리 정의하지 않으면 에러