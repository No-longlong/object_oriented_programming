
# 데코레이터 함수: 함수를 받아서 그 함수를 꾸며주고 꾸며진 함수를 리턴한다.
def add_print_to(original): # 데코레이터 함수, 파라미터로 어떤 함수를 받아서 또 다른 함수로 리턴
    def wrapper():
        print('함수 시작')
        original() # print_hello() 함수를 호출한 것과 같다.
        print('함수 끝') # 함수 시작과 함수 끝이 print_hello 라는 기존의 함수를 꾸민 것
                        # 이것이 데코레이팅 개념
    return wrapper

@add_print_to # 프린트 함수를 add_print_to로 꾸며주라는 의미(데코레이터)
def print_hello():
    print('안녕하세요')


# add_print_to(print_hello) # 이대로 하면 결과가 출력 안됨
                            # wrapper라는 함수를 리턴했기 때문에
                            # wrapper를 호출하기 위해서는 괄호를 붙여줘야 한다.
# 방법1
#add_print_to(print_hello)() # 함수인 print_hello를 인자로 주는 것과
                            # 함수를 호출하는 것인 print_hello()를 파라미터로 주는 것은 다르다.
                            # print_hello()의 리턴값은 None이므로 None값을 주는 것
                            # print()와 Return은 엄연히 다른 개념

# 방법2
# print_hello = add_print_to(print_hello)
# print_hello()

# 방법3 데코레이터 골뱅이를 활용
print_hello()