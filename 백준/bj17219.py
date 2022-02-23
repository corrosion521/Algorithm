import sys

n,m = map(int,input().split())

d1 ={}

for i in range(n):
    a,b=sys.stdin.readline().split()
    d1[a] = b

for j in range(m):
    print(d1[sys.stdin.readline().strip()])

