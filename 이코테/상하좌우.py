'''
구현
1.판 지정
2.이동에 따른 조건문 지정
'''
x=1# 최초 x
y=1# 최초 y
move =[]# 이동 리스트

# 판 지정
n = int(input())

# 이동 리스트 
move = list(input().split())

# 이동 실행
for i in move:
  if i == 'L' and y-1>0:# 한계지정
    y-=1
  elif i =='R' and y+1<=n:
    y+=1
  elif i =='U' and x-1>0:
    x-=1
  elif i =='D' and x+1<=n:
    x+=1

print(x,y)
    
