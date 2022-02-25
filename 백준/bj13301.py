'''
합의 합- dp
1.규칙성
길이 :
1개-4
2개-6
3개-10 = 4+6
4개- 16 = 10 + 6
5개 - 26  16
'''
def all_t(n):
    if n<=2: # n이 2보다 작아도 기본 배열은 존재하도록
        dp=[0]*3
    else:
        dp = [0] * (n + 1)
    # 기본 배열 3개
    dp[0] = 0
    dp[1] = 4
    dp[2] = 6

    if n>=3: #규칙성 따르는 dp[3]부터 
        for i in range(1,n-1):
            dp[i+2] =dp[i]+dp[i+1]

    return dp[n] # 출력

n = int(input())

print(all_t(n))
