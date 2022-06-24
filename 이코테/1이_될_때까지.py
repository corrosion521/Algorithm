'''
greedy
1. 1빼기 혹은 k로나누기인데
2. 나누기가 더 회수를 줄일 수 있음
3. 다만, 나누어떨어질때만
'''

n,k = map(int,input().split()) 
count=0 
while n!=1 :
  count+=1 
  if n%k==0:
    n= n//k
  else:
    n-=1
print(count)