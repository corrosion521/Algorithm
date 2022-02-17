'''
1. list() : 반복가능한(iterable) 자료형 s를 받아 리스트로 돌려주는 함수.
1) map과 쓰이는 경우 있음
2) string과 같은 iterable과 같이 쓰임
'''

import sys

n = int(input())
a=[]


for i in range(n):
    a = list(sys.stdin.readline())#string받아서 리스트화
    a.pop()# 개행지우기
    vps = 0 # vps판별기

    for i in range(len(a)):
        if a[i]=='(': # (일때
            vps+=1 # 1증가, 후에 -1되어 0이 되어야함
        else: # )일때
            if vps==0 :# 시작지점이거나, 완벽하게 앞에서 짝을 이루었는데 ) 나오면 절대 vps성립 안됨.
                vps-=1
                break
            vps-=1

    if vps==0:
        print("YES")
    else:
        print("NO")