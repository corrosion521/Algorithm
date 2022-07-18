'''
dfs

0. g, v
1. visit
2. push
3. 검사
4. pop

풀이?:
1. visit,push,pop은 같지만
2. 검사의 과정이 상하좌우로 뻗어나간다는 차이가 있다.
3. 전부 뻗어나가고 (전부 pop)되면 result를 하나씩 증가시킨다. 
'''

# N,M을 공백으로 구분하여 입력받기
n,m = map(int,input().split())

# 0. g+v
# 2차원 리스트의 맵 정보 입력받기
graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

  
# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x<= -1 or x>= n or y <= -1 or y>=m:
    return False

  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    # 해당 노드 방문 처리(1.visit)
      graph[x][y] = 1 
      # 상,하,좌,우의 위치도 모두 재귀적으로 호출
      
      # 2. push (출력은 x)

      # 3. 검사 2 - 뻗어나가기
      dfs(x-1, y)
      dfs(x,y-1)
      dfs(x+1, y)
      dfs(x, y+1)
      # 결과와 연관
      return True
    
  # 4. pop
  return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0

#3.검사 1 - 하나씩 검사
for i in range(n):
  for j in range(m):
    # 현재 위치에서 DFS수행
    if dfs(i,j)==True:
      result +=1

print(result) # 정답 출력