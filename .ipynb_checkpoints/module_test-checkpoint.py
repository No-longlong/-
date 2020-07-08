'''
    모듈명 : module_test
    mean : 리스트 평균
    calc : 두 수의 사칙연산 결과
'''
# 리스트 평균
def mean(nums):
    return sum(nums) / len(nums)

# 사칙연산
def calc(x, y):
    add = x + y
    diff = x - y
    mult = x * y
    div = x / y
    return add, diff, mult, div