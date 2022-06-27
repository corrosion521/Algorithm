'''
구현
1. 하나 바꿈(좌우든 상하든)
2. 가장 많은 연속된 것 하나 출력

어려운점
1. 판 생성 (2중 리스트)
ex)board =[list(input()) for i in range(n)]#판 생성
2. 규칙 파악이 제일 중요(당연) 이를 이해하기 어렵다면, 예시와 함께라도 이해해라. 그냥 넘기만 반드시 틀림
ex) 하나 바꾸고, 연속된(->,아래)것 확인이라는 규칙
ex2) 하나 바꿀 때, 아래,우측이랑만 바꾼다는 규칙성 확인.
3. for j in range(1,n)
'''


def check(board):
  n = len(board)# 행 개수
  ans =0 # 연속된게 없다면.. (하나짜리라면) 하나도 못먹음 그래서 0
  for i in range(n):
    cnt = 1 # 굳이 1인 이유: 하나 연속되면 cnt가 2가 되야함(이게 ans까지 이어짐)
    ex=1 # 이하동문
    for j in range(1,n):
      if board[i][j] == board[i][j-1]:#해당 행(좌우) 하나씩 비교
        cnt +=1
      else: 
        cnt = 1 # 다르면 연속 끊어져서 1로 초기화됨
      if ans<cnt : # 연속이 있다면, 없을 때 이걸 적용하면 ans가 1이되는데, 1개만 집어먹는 경우는 없으므로 x
        ans =cnt  # 출력
        
      if board[j][i] == board[j-1][i]:# 해당열 하나씩 비교
        ex+=1
      else: ex=1 # 이하동문
      if ans<ex: ans=ex # 연속이 있는 동시에 좌우 비교보다 크면 ex로 출력
  return ans
  

n = int(input())#판 크기 

board =[list(input()) for i in range(n)]#판 생성
ans = 0
# 계산
for i in range(n): 
  for j in range(1,n):#1.하나바꿈 !   1이 있는 이유 : 좌 우 교환,위 아래 염두해보자(마지막 부근)
    board[i][j],board[i][j-1] = board[i][j-1],board[i][j] # 1-1. 오른쪽과 교환
    temp = check(board) #2.check !   좌우 바꿨을 경우,체크

    if ans<temp: #2. 뭔가 답이 들어왔다!
      ans = temp
    board[i][j],board[i][j-1] = board[i][j-1],board[i][j] # 원위치,오른쪽과 교환
    board[j][i],board[j-1][i] = board[j-1][i],board[j][i] #1-2.  위 아래 교환
    temp = check(board)
    if ans<temp : 
      ans=temp
    board[j][i],board[j-1][i] = board[j-1][i],board[j][i] # 원위치,위 아래 교환
print(ans)


    

      