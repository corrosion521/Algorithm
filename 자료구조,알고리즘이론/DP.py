'''
1.DP(Dynamic Programming):
1)피보나치 수열처럼 이미한 연산(재귀로 인한)이 반복되는 결점을 보완키위해
동적 계획법 (Dynamic programming,dp)가 고안되었다.
2)원리
1> 계산 기록보관함 생성(Memoization)
2> 처음 진행되는 연산은 기록, 이미 진행된 연산은 다시 연산하는 것이 아니라 기록되어 있는 값을 가져옴.
3)종류 -예시를 보는게 빠름
1>Top Down : 문제 해결이 위->아래(큰 계산->작은 계산)
2>Bottom Up : 아래->위(작은 계산->큰 계산)
3)VS 그리디 알고리즘
1>그리디 알고리즘은 모든 해를 그때마다 최적의 해를 구함. 최종적으로 최적의 해라고 장담은 할 수 없다.
2>DP는 모든 방법(모든 계산)을 다해 최종적으로 최적의 해를 구함
'''

# 일반 피보나치 수열: 재귀로 인한 중복계산들이 발생한다.
def fib(n):
  if n<=2:
    return 1
  else:
    return fib(n-1)+fib(n-2)

n = int(input())
print(fib(n))

# DP 피보나치 수열: 중복 계산을 피한다.(Top down,memoization)

l1=[0]*100 #1> 중복계산을 피하기 위한 계산기억 보관함.

def fib(n):
  if n<=2:
    return 1
  if l1[n]==0: # 2> 보관함에 기록되지 않았으면 계산, 기록되어있으면 계산안함
    l1[n]= fib(n-1)+fib(n-2)
  return l1[n] # 정답 꺼내서 반환

n = int(input())
print(fib(n))

# DP 피보나치 수열: Bottom up

def fib(n):
  fi=[0]*100
  fi[0] = 1
  fi[1] = 1
  for i in range(n-2):
     fi[i+2]=fi[i]+fi[i+1]

  return fi[n-1]

print(fib(int(input())))