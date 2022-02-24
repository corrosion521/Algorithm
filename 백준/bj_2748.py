'''
dp - bottom up
1. 주의 : 수의 범위 유의할 것
입력값이 반드시 함수를 사용하게 되는지..
'''

def fib(n):


    for i in range(n-1):
            dp[i+2] = dp[i+1] + dp[i]

    return dp[i+2]


n = int(input())

dp=[0]*(n+1)
dp[0]=0# 0
dp[1]=1# 1
if n>1:
    print(fib(n))
else:
    print(dp[n])

