'''
1. 동적인 자료는 덱(스택,큐)을 이용하는 게 훨씬 편하다
1) 덱 안쓴 코드
N, K = map(int, input().split())

li = list(range(1,N+1))

x = K-1 # x는 타겟 인덱스 값

print("<",end="")

for i in range(N):
    print(li.pop(x),end="")
    x +=K-1 #0대신 새로운 초기값 x에 K-1 더함
    if len(li)!=0: # 하나 남기 전까지
        while x >len(li)-1: # 인덱스가 리스트를 넘으면
             x-=len(li) # 인덱스를 리스트 개수만큼 빼줌
        print(", ",end="")

print(">")

2. 덱은 deque([1, 2, 3, 4, 5, 6, 7]) 이런식으로 출력됨.
1) popleft(appendleft), pop(appendleft)로 구성
2) 특정인덱스 pop,append불가
3) 리스트 앞쪽 (왼쪽)이 기본적으로 구조상 바닥
'''
from collections import deque

N, K = map(int, input().split())

q1 = deque()

# 큐 채워넣기
for i in range(1,N+1):
    q1.append(i)

# 큐에 하나라도 남아 있는 이상!
print("<",end="")
while True:
    for i in range(K-1): # 타겟 이전 것들 다 뺴버리자
        q1.append(q1.popleft())# 큐에서 뺸것을(왼쪽) 오른쪽으로 다시 append
    print(q1.popleft(),end="")# 얜 K번째(K-1인덱스)그냥 빼버림(삭제)
    if len(q1)==0:
        break
    print(", ",end="")
print(">",end="")













