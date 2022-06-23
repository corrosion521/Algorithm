'''
greedy
=>
1. 1부터 차례로 더해감
2. 초과한 경우 이전에 더한 수를 빼고 다시더함(count-1)
2-2. 2의 경우를 거치고도 다시 초과하면
다시 한번 더빼고(count-2)
더함
=> 2의 과정은 수의 법칙상 사실 상 고정적임(count-=2 , count+=1)

'''

a = int(input())


sum = 0
plus = 1# 처음, 가장 작은 자연수 1
count = 0 # 더해진 횟수
while True:
  sum +=plus
  count +=1
  plus+=1

  if sum>a:
    if plus>=sum-a:
        count-=1
        break
    
  if sum==a :
    break
  
  
print(count)