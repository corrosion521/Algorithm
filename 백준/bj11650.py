'''
1. 정렬 - ( ) 괄호 이용하여 다중 키값 지정. 이 때 앞에 있는 것이 우선 기준

'''



N = int(input())

t=[]

for i in range(N):
   t.append(list(map(int,input().split())))

t.sort(key=lambda x:(x[0],x[1]))



for a in range(N):
     print(t[a][0],t[a][1])