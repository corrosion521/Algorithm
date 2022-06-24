'''
greedy
1. 한 행씩 계산하여 최소값 탐색
2. 이 최소값 리스트에 넣음
3. 리스트 중 최대값

'''
l1=[]# 각 행별 최소값 리스트


n,m = map(int,input().split())# 행 열 입력

for i in range(n):
   l1.append(min(list(map(int,input().split()))))

print(max(l1))