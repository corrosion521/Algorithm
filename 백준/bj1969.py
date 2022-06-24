'''
greedy
1. 여러 문자열의 문자들을 조사하면서 가장 많은 문자를 추출해낸다
2. 동시에 이에 대한 Distance를 더해나간다.
3. 사전순정렬-> Distance 같은 경우는 if문으로 ...
'''

distance = 0
l1 =[]

rl=[]

n,m= map(int,input().split())

for i in range(n):
  l1.append(input())

for i in range(m):
  m =0
  al=[0,0,0,0]
  
  for j in range(n):
    if l1[j][i]=='A' :
      al[0]+=1
    elif l1[j][i]=='C' :
      al[1]+=1
    elif l1[j][i]=='G' :
      al[2]+=1
    elif l1[j][i]=='T' :
      al[3]+=1
      
  if max(al)==al[0]:
    distance += n-max(al)  
    print("A",end='')
  elif max(al) ==al[1]:
    distance += n-max(al)  
    print("C",end='')
  elif max(al) == al[2]:
    distance += n-max(al)  
    print("G",end='')
  elif max(al) == al[3]:
    distance += n-max(al)  
    print("T",end='')  

print()
print(distance)