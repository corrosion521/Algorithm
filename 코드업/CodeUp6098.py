'''
조건 문
1. if elif else 관계성 유의
제대로 필터링 안될 수 있음
ex)
if
if
else(x)

if
elif
else(o)

'''

# 빈 미로 생성
maze = [[0 for i in range(10)]for i in range(10)]


# 미로 입력
for i in range(10):
    a = list(map(int,input().split()))
    for j in range(10):
        maze[i][j] = a[j]



# 1. 시작(2,2)
# 2. 1)우 하단 움직일 수 없는 경우, 2)먹이 찾은 경우 -> 머무르기
x,y=1,1
maze[x][y] = 9
while(True):
    if maze[x][y+1]==0:# 오른쪽 이동 가능 시 이동(먹이x)
        maze[x][y+1]=9
        y+=1
    elif maze[x][y+1]==2:#2)오른쪽 이동 가능(먹이 o)
        maze[x][y+1]=9
        break
    else: #오른쪽 이동 불가 시..
        if maze[x+1][y]==0 : # 하단 이동 가능(먹이 x)
            maze[x+1][y]=9
            x+=1
        elif maze[x+1][y]==2:#2) 하단 이동 가능(먹이 o)
            maze[x+1][y]=9
            break
        else: # 1)움직일 수 없는 경우(우하단)
            break

# 미로 출력
for i in range(10):
    for j in range(10):
        print(maze[i][j],end=" ")
    print()