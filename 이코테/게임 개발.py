'''
구현

1. 판: nxm
2. 칸: 육지 or 바다
3. 캐릭터 : 
1)동서남북 바라봄
2)상하좌우 움직임
3)바다 못감
4. 행동 :
1) 반시계 90도 회전 
2)
1 - 다 가봄 : 1)로 복귀
2 - 한 칸 이동
3) 다 돌아도(반 시계90x4) 다가본거면 뒤로 1칸 -> 1)로 복귀

어려웠던 점
1. 변수와 주석을 잘 달자
2. 복붙때문에 코드가 더러워졌다. 즉 다시말해 
코드가 꼬인 것이다.
이런 경우는 차라리 처음부터 다시 디버깅(머리속으로) 해보자.

'''
# map. 2차원 배열 염두
game_map = [] 
cnt=1 # 처음에 밟고 있는 곳 1 

# nxm 입력
n,m= map(int,input().split())

# 캐릭터 좌표, 방향 입력
a,b,d = map(int, input().split())

# map 데이터 입력

for i in range(n):
     game_map.append(list(map(int,input().split())))

game_map[a][b]= 1
# 게임

while True:
  d-=1 # 1. 우선 반시계방향 회전 
  if d<0:# 북 <- 서
    d=3

    
  # 현재 서 바라볼 떄
  if d==3: 
    # 이동가능
    if game_map[a][b-1]!=1:
      game_map[a][b-1] = 1  # 이동한 곳은 1로 바꾸기
      cnt+=1 #이동 카운트 up
      b-=1 # 당연히 좌표도 따라 이동
  # 아래 케이스도 모두 동일
  # 현재 동 바라볼 떄
  if d==1: 
    # 이동가능
    if game_map[a][b+1]!=1:
      game_map[a][b+1] = 1    
      cnt+=1
      b+=1
  # 현재 남 바라볼 떄
  if d==2: 
    # 이동가능
    if game_map[a+1][b]!=1:
      game_map[a+1][b] = 1    
      cnt+=1
      a+=1

  # 현재 서 바라볼 떄
  if d==3: 
    # 이동가능
    if game_map[a-1][b]!=1:
      game_map[a-1][b] = 1    
      cnt+=1
      a-=1
    
  # 동서남북 모두 1일 떄
  if game_map[a-1][b]==1 and  game_map[a+1][b]==1 and  game_map[a][b+1]==1 and  game_map[a][b-1]==1:
    break

print(cnt)
