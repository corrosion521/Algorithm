'''
dfs
0. g,v
1. visited
2. push 
3. 검사 - 재귀
4. pop

부족했던 점
1. 연결관계- 양쪽이 각각 리스트에 상대방을 가지고 있어야함.
=> 조건문 not in 을 통해서 표현할 수 있음.
'''

def dfs(graph,v,visited,stack):
  visited[v]=True
  stack.append(v)
  
  
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited,stack)

cpu_number= int(input())
link_number = int(input())
graph=list()


for i in range(cpu_number+1):
  graph.append([])
for i in range(link_number):
    start_v,link_v = map(int,input().split())
    if  link_v not in graph[start_v]:
      graph[start_v].append(link_v)
    if  start_v not in graph[link_v]:
      graph[link_v].append(start_v)

visited=[False]*(cpu_number+1)

stack=[]
dfs(graph,1,visited,stack)

print(len(stack)-1)