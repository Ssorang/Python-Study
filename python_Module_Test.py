import sys

print(sys.path)

print(type(sys.path))

# 모듈 경로 삽입
# sys.path.append('/Users/sorang/StudyCode/Python/python_Module.py')

# print(sys.path)

# import python_Module as pm

# 모듈 사용

# print(pm.power(10,3))

import python_Module as pm

print(pm.divide(1324,52))