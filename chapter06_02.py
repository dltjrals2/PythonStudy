# Chapter06-2
# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

# print('-' * 15)
# print('Called! inner!')
# print(add(5, 5))
# print(subtract(15, 5))
# print(multiply(5, 5))
# print(divide(5, 5))
# print(power(5, 3))
# print('-' * 15)

# __name__ 사용
# 모듈이 import가 아닌 자기 자신에서 돌렸을때만 돌아간다.
if __name__ == "__main__":
    print('-' * 15)
    print('Called! inner!')
    print(add(5, 5))
    print(subtract(15, 5))
    print(multiply(5, 5))
    print(divide(5, 5))
    print(power(5, 3))
    print('-' * 15)
