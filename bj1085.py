'''
현 위치 (x,y)일 때  왼쪽 아래 꼭지점 0,0 , 오른쪽위 꼭지점(w,h)인 직사각형(좌표평행)
직사각형의 경계선가지 가는 거리의 최소값?
점에서 세로, 가로의 길이 둘 중하나가 최소값이 된다.
1) 세로 에서 좌, 우 까지의 거리 비교 후 선택
2) 가로 역시 마찬가지
3) 1) 2) 중 최소값 선택.
'''

# 입력: 1<=x<=w-1 ,1<=y<=h-1 , 최대치가 w,h로부터 -1씩은 떨어져있어야함.
# 1<=w,h<=1000
x,y,w,h=map(int, input().split())

'''
sero = 0
garo = 0
result = 0
# 계산: 세로 좌vs우
if w-x>x :
    sero = x
else:
    sero = w-x

# 계산 2 : 가로 좌vs우
if h-y>y :
    garo = y
else:
    garo = h-y

# 계산 3 : 세로vs가로
if sero>garo:
    result = garo
else:
    result = sero
'''

# 출력: 결과
print(min([x,y,w-x,h-y]))

'''
뭐 조건문 나쁘진 않지만...
파이썬은 min(list)이라는 내장함수가 있다는 것을 명심하자

'''

