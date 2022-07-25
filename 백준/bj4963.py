import sys

sys.setrecursionlimit(5000000)
'''
dfs

0. g, v
1. visit
2. push
3. 검사
4. pop

어려웠던점
1. setrecursionlimit설정
2. x,y구분 잘하기

'''


def dfs(x, y):
    # 범위 벗어나는 경우 건너뛰기
    if y < 0 or y >= w or x < 0 or x >= h:
        return False
    # 바다인경우 건너뛰기
    # if graph[x][y]==0:
    #     return False

    # 섬인경우 재귀
    if graph[x][y] == 1:
        #방문처리
        graph[x][y] = 0
        # 상하좌우 탐색
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        # 대각선 탐색
        dfs(x - 1, y - 1)
        dfs(x - 1, y + 1)
        dfs(x + 1, y - 1)
        dfs(x + 1, y + 1)
        return True
    return False


while True:
    w, h = map(int, input().split())

    if w == 0 & h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                result += 1
    print(result)
