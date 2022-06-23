'''
1. greedy
1) 현재 상황에서 최선의 선택
=>
1. 리스트 중 가장 큰 수 K번 더하기
2. 이후, 그 다음으로 큰 수 K번 더하기
3. 이후 다시 가장 큰 수 K번...
'''
result = 0
N,M,K = map(int,input().split())

l1 = list(map(int,input().split()))


m1 = max(l1) # 리스트 중 가장 큰 수
l1.remove(m1)# 그 수 제거

m2= max(l1) # 두 번째 로 큰 수
count = 0
plus = m1
for i in range(M):
  
  result += plus
  count +=1

  if count==K and plus == m1:
    plus = m2
    count = 0
  elif count == 1 and plus == m2:
    plus = m1
    count = 0
print(result)