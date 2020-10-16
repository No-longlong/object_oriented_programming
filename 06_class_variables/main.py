class User:
    count = 0 # 클래스 변수, 한 클래스 내의 모든 인스턴스가 공유하는 속성
    def __init__(self, n, m, p):
        self.name = n
        self.email = m
        self.password = p
        User.count += 1

user1 = User("노아씨", 'meorn@naver.com', '****')
user2 = User("아씨", 'meorfdfn@naver.com', '**aaa**')
user3 = User("아저씨", 'mefasdfrn@naver.com', '**fdsfasf**')

# 클래스 변수 값 설정 #################################
# user1.count = 5 이것은 클래스 변수가 아닌 인스턴스 변수 설정.
# 원래 이것을 설정안하고 출력했으면 클래스 변수인 3이 출력되어야 정상
# 같은 클래스 변수 vs 같은 인스턴스 변수 라면,
# 인스턴스 변수가 더 우선된다.
# 이런 경우 문제가 발생할 수 있으므로,
# 클래스 변수를 설정할때는 클래스 이름을 통해서(인스턴스가 아닌) 클래스 변수를 설정해줘야 한다.
# user.count = 5 --> X
User.count = 5 # 클래스 변수를 통해 클래스 변수 값 변경

# 클래스 변수 읽기 1. 클래스이름.클래스변수 2. 인스턴스이름.클래스변수
# 클래스 변수 설정하기 1. 클래스이름.클래스변수

print(User.count)
print(user1.count)
print(user2.count)
print(user3.count)