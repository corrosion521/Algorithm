'''
1. 그냥 팩토리얼
import math,
math.factorial()써도 상관없음.
'''


def factorial(n):
    if n >=1:
        return factorial(n-1)*n
    else:
        return 1

n = int(input())

n= str(factorial(n)) # 문자화

count=0 # 카운터

for i in range(len(n)-1,-1,-1): # 뒤에서 부터 올라가며 점검
    if n[i] != '0':
        break
    count += 1

print(count)