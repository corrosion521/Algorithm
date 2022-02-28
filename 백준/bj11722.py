'''
dp
'''

n = int(input())

l1 = list(map(int,input().split()))

dp= [1]*n

for i in range(n):
    for j in range(i):
        if l1[i]<l1[j]:
           dp[i] =max(dp[i],dp[j]+1)

print(max(dp))