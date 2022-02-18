'''
1. 시간복잡도 줄이기(for문 등)- 이진탐색 등으로 줄여나가자.
=> 이진탐색 sort()해줘야함 까먹지마라.
2. []*8 리스트안생김. [0]*8 로 해주자.
3. collections모듈 - Counter: 배열에 있는 원소의 개수를 세서 딕셔너리 형태로 반환해줌
ex) arr=[1,2,3,4]
count = Counter(arr)
print(count) # Counter({1:1,2:1,3:1,4:1})
'''
import sys
from collections import Counter

n = int(sys.stdin.readline())
n_list = Counter(list(map(int,sys.stdin.readline().split())))

m = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().split()))

for i in range(m):
        if m_list[i] in n_list:
            print(n_list[m_list[i]],end=" ")
        else:
            print("0",end=" ")



