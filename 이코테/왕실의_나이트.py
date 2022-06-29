'''
구현

1. 이동 가능 방향
1) 우2 -> 위1 아래1
2) 좌 2->위 1 아래1
3) 상 2-> 우1 좌 1
4) 하 2 -> 우 1 좌1
==> full 이면 8개인데..
2. 범위를 넘어서는 경우
ex) 1미만 8초과
ex) a아래, h초과
-> count -?
'''

n=input()

row = int(n[1]) # 행
col = n[0] # 열
count = 0
# 상하좌우 이동 필터 

# 1) -위 
if ord(n[0])+2<=ord('h') and row-1>=1:
  count+=1
# 1) 아래
if ord(n[0])+2<=ord('h') and row+1<=8:
  count+=1

# 2) 위
if ord(n[0])-2>=ord('a') and row-1>=1:
  count+=1

# 2) 아래 
if ord(n[0])-2>=ord('a') and row+1<=8:
  count+=1

# 3) 우 
if ord(n[0])+1<=ord('h') and row-2>=1:
  count+=1

# 3)좌
if ord(n[0])-1>=ord('a') and row-2>=1:
  count+=1

# 4) 우
if ord(n[0])+1<=ord('h') and row+2>=1:
  count+=1

if ord(n[0])-1>=ord('a') and row+2<=8:
  count+=1


print(count)