'''
1. 브루트 포스(brute force) : 조합 가능한 모든 문자열을 하나씩 대입하여 암호를 해독해나가는 방식
무차별 대입 공격.
2. 바둑판(행열판): 엔터 고려해서 행만 이용으로 가능
3. 검사 : 처음부터 훑기 (눈으로 훑어서 인식하지 못했지만 사실은 반복문의 개념) . 반복문 사용(FOR,WHILE등)
4. 기능의 분류 : for문- 시작점, 내부에 바둑판 , 그 내부에 판별 조건문들...
+ 판별 조건문들 중, 케이스 분류(1. W시작,B시작 2.짝수 행열 부분, 홀수 행열 부분)중요.
또한 조건들의 위계(짝-W시작,B시작 등)도 유연하게 생각하자. 인간의 논리가 아니라 컴퓨터의 논리로.
'''

N,M = map(int,input().split()) # 행,열 입력
org=[]
count=[] # 카운트 리스트
for i in range(N):# 입력판 입력, 2.
    org.append(input())

# 3.
# 0~N-7까지가 시작점의 후보
# 시작점으로부터 끝까지 시작점포함 8개는 있어야함 (8X8을 뽑아내야하므로)
for i in range(N-7):# 시작점(행)
    for j in range(M-7): # 시작점(열)
        wc = 0 # 'W' 시작- change  count
        bc = 0 # 'B' 시작- change  count
        for a in range(i,i+8): # 지정된 바둑판 열
            for b in range(j,j+8): # 지정된 바둑판 행
                if (a+b) % 2== 0 : # i+j 짝수 위치일 경우
                    if org[a][b] != 'W': # W가 시작일 경우
                        wc += 1 # W시작이면 i+j위치는 모두 W여야 되는데 아니므로 바꿀 카운트
                    else: # B가 시작일 경우
                        bc += 1 # B시작이면 i+j위치는 모두 B여야 되는데 아니므로 바꿀 카운트

                else: #i+j 홀수위치인 경우
                    if org[a][b] != 'B': # W가 시작일 경우
                        wc += 1 # W시작이면 i+j위치는 모두 W여야 되는데 아니므로 바꿀 카운트
                    else: # B가 시작일 경우
                        bc += 1 # B시작이면 i+j위치는 모두 B여야 되는데 아니므로 바꿀 카운트

        count.append(min(wc,bc)) # 한 지점으로 정한 8x8판 안에서, W시작,B시작의 경우 중 작은 것을 고름.

print(min(count)) # 카운트리스트 중에서도 가장 작은 것



