'''
1. sort(): 반환하지 않고 그대로 정렬해줌.
2. sys.stdin.readline() : 줄 단위로 입력을 받음. 개행이 들어가야됨.
'''
import sys

N = int(input()) # 주어지는 수의 개수

li=[] # 리스트

# 입력
for i in range(N):
        li.append(int(sys.stdin.readline()))

# 정렬
li.sort()

# 출력
for i in range(N):
    print(li[i])