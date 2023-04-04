# *args(언팩킹) / enumerate 인덱스와 원소를 짝지어줌 0 A -> 1 B -> 2 C 이런식으로
def args_func(*args):
    for i, v in enumerate(args): # 매개변수 명 자유
        print('Result : {}'.format(i), v)
        print(f'i : {i}, v : {v}')
    print('-----------')

args_func('Lee')
args_func('Lee','Park')
args_func('Lee','Park','Kim')

# **kwargs(언팩킹)
def kwargs_func(**kwargs): # 매개변수 명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-----------')

kwargs_func(name1="Lee")
kwargs_func(name1="Lee", name2='Park')
kwargs_func(name1="Lee", name2='Park', name3='Cho')


# 중첩함수

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)