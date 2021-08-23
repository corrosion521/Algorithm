'''

세 점이 주어 졌을 때, 축에 평행한 직사각형을 만들기 위해
필요한 <<네번째점을 찾는거?>>
x,y좌표 : 1개만 있는 좌표의 x,y와 동일

'''
listx=[]
listy=[]
for i in range(3):
    a,b = map(int,input().split())
    listx.append(a)
    listy.append(b)

for i in range(3):
    if listx.count(listx[i])==1:
        x = listx[i]
    if listy.count(listy[i])==1:
        y = listy[i]

print(x,y)

'''
count() 함수..
'''