'''
1. 리스트 컴프리헨션 : 한 줄로 이중리스트 생성 가능
   ex)d = [[0 for i in range(19)] for i in range(19)]
2. d = [0*19]*19 와 같은 형식으로 배열을 선언하면, 요소를 복사하는
shallow copy가 발생한다. 요소를 초기화 시키지 않는 경우는 상관 없지만, 초기화한다면
복사가 발생하므로 유의해야 한다.
단, [[0]*19for i in range(19)]와 같은 경우는 상관없다.
<https://infinitt.tistory.com/106>
'''


# 빈 바둑판 만들기
# d=[]
# for i in range(19):
#     d.append([])
#     for j in range(19):
#         d[i].append(0)

#d = [[0 for i in range(19)] for i in range(19)]

d= [[0]*19for i in range(19)]


# 바둑판 기록
n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    d[x-1][y-1] = 1

# 바둑판 출력
for i in range(19):
    for j in range(19):
     print(d[i][j],end=' ')
    print(end='\n')