# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(Lamda

# 함수 정의 방법
# def funtion_name(parameter):
#   code

# 에제1

def first_func(w):
    print("Hello, ", w)

wrod = "Good boy"

# 예제2 

def return_func(w1):
    value = "Hello, " + str(w1)

x = return_func

# 람다식 예제
# 장점 : 메모리 절약, 가독성 향상, 코드 간결
# 단점 : 
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기호) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

#def mul_func(x, y):
#   return x * y

#lambda x, y: x*y

def mul_func(x, y):
    return x * y

q = mul_func(10, 50)
print(q)

mul_func_var = mul_func
print(mul_func_var(20,50))

lambda_mul_func = lambda x,y:x*y

print(lambda_mul_func(50, 50))

def func_final(x, y, func):
    print(x * y * func(100, 100))

func_final(10, 20, lambda x,y:x*y)