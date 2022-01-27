'''
1. 빈 리스트 만들 때, 가로(행) 세로(열) 제대로 만들기..
이차원 리스트는 [ [],[],[]... ]라는 구조 명심하자.(내부의 내부가 존재하는 구조)

'''

# 격자판
h,w = map(int,input().split())
board=[[0 for i in range(w)] for i in range(h)]

# 막대 개수
n = int(input())
for i in range(n):

# 막대길이, 방향, 좌표
    l,d,x,y = map(int,input().split())
    x-=1# x,y좌표 1부터 시작하는 것 염두
    y-=1
    if d==0:# 가로
            for y in range(y,y+l):
                board[x][y] = 1
    else: # 세로
            for x in range(x,x+l):
                board[x][y] = 1



#출력
for i in range(h):
    for j in range(w):
        print(board[i][j],end=" ")
    print("")