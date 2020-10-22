class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod # 클래스 메소드 설정
    def from_string(cls, string_params):
        # 첫번째 인자는 cls 규칙 준수
        # string을 나눠서 class에 return
        split_user = string_params.split(",")
        name = split_user[0]
        email = split_user[1]
        password = split_user[2]
        return cls(name, email, password)

    @classmethod # 클래스 메소드 설정
    def from_list(cls, list_params):
        name = list_params[0]
        email = list_params[1]
        password = list_params[2]
        return cls(name, email, password)
# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)