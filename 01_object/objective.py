class User:
    def say_hello(self):
        print(f"안녕하세요 {self.name}입니다.")

    def check_name(self, name):
        return self.name == name

