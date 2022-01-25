'''
for i in range( , ,!!)
!!: 이거 안쓰면 디폴트가 1 이라는 점 기억하자.
'''
n = int(input())
list = list(map(int,input().split()))

for i in range(n-1,-1,-1):
    print(list[i],end=" ")

