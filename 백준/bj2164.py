'''
1. 큐: FIFO(First In First Out)
1) pop(0) : 첫 번째 데이터 제거 가능.
2) range(1,N): 이를 이용하여 반복문 없이 일정 범위 사용 가능

2. 덱(deque,Double Ended Queue):
1) 큐,스택 둘 다 만들 수 있는 자료구조. 양 끝단에서 모두 push,pop가능.
2) popleft() - 큐의 pop
3) deque() - 덱. 리스트에 담아 사용 가능.
4) from collections import deque - collections모듈로부터 모두 deque를 import

'''
from collections import deque

N = int(input())

li = deque() # 덱 담기

for i in range(N): # 카드 생성
    li.append(i+1)

while len(li)>1:# 카드 한장 남을 때 까지 반복
    li.popleft()# 1. 카드뽑음.
    li.append(li.popleft())# 2. 1과정 후 맨앞의 카드를 다시 리스트 뒤로 넣음.

print(li[0]) #한 장 남은 카드 번호 출력




