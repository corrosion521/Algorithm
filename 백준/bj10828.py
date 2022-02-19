'''
1. 파이썬은 따로 stack 구조를 재공하지 않음. list를 이용해서 표현 가능하다.
'''

import sys

n = int(input())

stk=[]

for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == "push":
        stk.append(a[1])

    elif a[0] == "pop":
        if len(stk)!=0:
            print(stk.pop())
        else:
            print("-1")

    elif a[0] == "size":
        print(len(stk))

    elif a[0] == "empty":
        if len(stk)==0:
            print("1")
        else:
            print("0")
    elif a[0] == "top":
        if len(stk) == 0:
            print("-1")
        else:
            print(stk[len(stk)-1])
