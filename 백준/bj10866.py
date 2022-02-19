'''
1. insert(a,b): 리스트에서 a번째 위치에 b를 삽입
a = [1,2]
a.insert(0,3)
a # [3,1,2]
'''

import sys

n = int(input())
deque =[]

for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == "push_front":
        deque.insert(0,a[1])

    elif a[0] == "push_back":
        deque.append(a[1])

    elif a[0] == "pop_front":
        if len(deque)!=0:
            print(deque.pop(0))
        else:
            print("-1")
    elif a[0] == "pop_back":
        if len(deque)!=0:
            print(deque.pop())
        else:
            print("-1")

    elif a[0] == "size":
        print(len(deque))

    elif a[0] == "empty":
        if len(deque)==0:
            print("1")
        else:
            print("0")
    elif a[0] == "front":
        if len(deque) == 0:
            print("-1")
        else:
            print(deque[0])
    elif a[0] == "back":
        if len(deque) == 0:
            print("-1")
        else:
            print(deque[-1])