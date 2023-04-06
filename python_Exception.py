# 예외처리
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError
# 문법적으로는 에외가 없지만, 코드 실행 프로세스(단계)발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다. -> 다른 곳으로 처리를 위임할 수 있다.
# 4. 예외 무시


# SyntaxError : 문법 오류

# print('Error)
# print('Error'))
# if True
#     pass


# NameError : 참조 없음

# a = 10
# b = 15
# print(c)


# ZeroDivisionError

# print(100/0)


# IndexError

# x = [50, 70, 90]
# print(x[3])
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())


# KeyError

# dic = {'name':'Lee', 'Age':41, 'City':'Busan'}
# print(dic['hobby'])
# print(dic.get('hobby')) 


# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAFP)


# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외

import time
# print(time.time2())


# ValueError

# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200) # 리스트 값이 없음


# FileNotFoundError

# f = open('test.xlsx')


# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우

# x = [1,2]
# y = (1,2)
# z = 'test'
# print(x + y)
# print(x + z)
# print(y + z)

# print(x + list(y))
# print(x + list(z)) # 형변환 시 가능



# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1 : 여러개 가능
# except 에러명2 
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

name = ['Kim', 'Lee', 'Park']

# 예제 1
# try :
#     z = 'Kim'
#     x = name.index(z)
#     print(f'{z} Found it! {x + 1} in name')
# except ValueError :
#     print('Not found it! - Occurred ValueError!')
# else :
#     print('Ok! else.')

# print()

# 예제 2

# try :
#     z = 'Kim'
#     x = name.index(z)
#     print(f'{z} Found it! {x + 1} in name')
# except Exception:
#     print('Not found it! - Occurred ValueError!')
# else :
#     print('Ok! else.')

# print()

# 예제 3

# try :
#     z = 'Cho'
#     x = name.index(z)
#     print(f'{z} Found it! {x + 1} in name')
# except Exception as e:
#     print(e)
#     print('Not found it! - Occurred ValueError!')
# else :
#     print('Ok! else.')
# finally:
#     print('Ok! Finally!')
      
# print()

# 에제 4
# 예외 발생 : raise
# raise 키워드로 에외 직접 발생

try :
    a = 'Park'
    if a == 'Kim' :
        print('OK! Pass!')
    else : 
        raise ValueError
except ValueError:
    print('Occurred! Exception!')
else:
    print('OK! else!')
