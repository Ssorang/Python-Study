# 클래스 개념
# OOP란 ? 객체 지향 프로그래밍
# 클래스, 인스턴스
# Self 개념
# 인스턴스 메소드
# 클래스, 인스턴스 변수

# 클래스 and 인스턴스의 차이 이해 
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 에제 1
class Dog(object): #모든 클래스는 오브젝트를 상속받는다.
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog("Chadol", 13)
b = Dog("baby", 3)
c = Dog("honey", 5)
d = Dog("baby", 3)

# 비교
print(b == d, id(b), id(d)) # 값은 같지만 id가 다르다 -> 파이썬이 같다고 인식 못함

# 네임 스페이스
print('dog1', a.__dict__)
print('dog1', b.__dict__)

# 인스턴스 속성 확인
print(f'{a.name} is {a.age} and {b.name} is {b.age}')

if a.species == 'firstdog':
    print(f'{a.name} is a {a.species}')

# 직접 접근
print(Dog.species) # 클래스로 접근
print(a.species)# 인스턴스로 접근
print(b.species)


# 예제 2
# self의 이해
class SelfTest:
    def func1():
        print('Func1 Called')
    def func2(self):
        print('Func2 Called')

f = SelfTest()

# print(dir(f))
print(id(f))
# f.func1() -> 예외
f.func2()

SelfTest.func1()
SelfTest.func2(f)


# 에제 3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수 = 0
    stock_num = 0 # 재고
    
    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)


# 에제 4
class Dog(object): #모든 클래스는 오브젝트를 상속받는다.
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return f'{self.name} is {self.age} years old'

    def bark(self, sound):
        return f"{self.name} says {sound}!"
    
# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Maary',10)
# 메소드 호출
print(c.info())
# 메소드 호출
print(c.bark('Wal Wal'))
print(d.bark('Mung Mung'))
