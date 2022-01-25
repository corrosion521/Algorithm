n = int(input())
list = list(map(int,input().split()))

fast=list[0]
for i in range(1,n):
    if list[i]<fast:
        fast=list[i]

print(fast)