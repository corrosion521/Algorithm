'''
1. 리스트
queue[len(queue)-1] = queue[-1] # 마지막, -0이 아니라 -1임을 유의하자.
2. pop():
1) argument 없을 경우는 리스트 가장 마지막 원소 빠져나감
2) 원소값은 인덱스를 넣어줌
ex)pop(0) # 첫번째 원소 pop
'''

import sys

n = int(input())

queue=[]

for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == "push":
        queue.append(a[1])

    elif a[0] == "pop":
        if len(queue)!=0:
            print(queue.pop(0))
        else:
            print("-1")

    elif a[0] == "size":
        print(len(queue))

    elif a[0] == "empty":
        if len(queue)==0:
            print("1")
        else:
            print("0")
    elif a[0] == "front":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])
    elif a[0] == "back":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[-1])