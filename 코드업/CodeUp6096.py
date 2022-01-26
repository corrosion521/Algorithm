'''
1. 엔터키로 input()의 입력을 한다는 점 생각해보자
'''


# 바둑판 생성
d=[]
for i in range(19):
    d.append([])
    for j in range(19):
         d[i].append(0)

# 바둑판 입력
for i in range(19):
    a = list(map(int,input().split())) # 1
    for j in range(19):
         d[i][j] = a[j]

# 십자 뒤집기
n = int(input())

for i in range(n):
    x,y = map(int,input().split())
    x-=1
    y-=1
    for i in range(19):# 뒤집기(가로)
            if d[x][i] == 0:
                d[x][i] = 1
            else:
                d[x][i] = 0
    for i in range(19):  # 뒤집기(세로)
        if d[i][y] == 0:
            d[i][y] = 1
        else:
            d[i][y] = 0


# 바둑판 출력

for x in range(19):
    for y in range(19):
        print(d[x][y],end=' ')
    print(end='\n')

