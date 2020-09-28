# # 가변 타입(리스트) vs 불변 타입(튜플)
#
# mutable_object = [1, 2, 3]
# immutable_object = (1, 2, 3)
#
# mutable_object[0] = 4
# print(mutable_object)
#
# immutable_object[0] = 4
# print(immutable_object) # 에러
#


# tuple_x = (6, 4)
# tuple_x[0] = 4
# tuple_x[1] = 1
#
# print(tuple_x) # 이미 생성된 객체의 값을 바꾸는 것은 에러

# tuple_x = (6, 4)
# tuple_x = (4, 1)
# tuple_x = (4, 1, 7)
#
# print(tuple_x)

# 정해진 튜플의 속성을 바꾸는 것은 에러 [(4, 1) --> 0번째를 3으로 바꿔라 (X)]
# 같은 변수 이름으로 튜플을 새롭게 할당하는 것은 가능

# 가변 타입
# list, dict

# 불변 타입
# bool, int, float, str, tuple

# 위는 파이썬의 클래스이고,
# 우리가 User() 처럼 직접 만든 class는 무슨 타입일까?
# 정답은 가변 타입
# 그래서 인스턴스 생성하면 속성을 바꿀 수 있으니,
# 새 인스턴스 만들지 않고 원래 인스턴스의 속성을 변경하면 된다.