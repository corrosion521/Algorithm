# 입력 : 도착지의 방(1<=n<=1000000000)
N = int(input())

# 계산:거리 2~7[1](6) : 2 8~19[2](6*2 ==12): 3 20~37(6*3 ==18): 4 38~61(6*4==24) : 5
r = 1
i = 1

while True: #범위 지정이 어려울 경우 for문이 아니라 while문 쓰는게 좋다.
    if i>=N:
        break
    i += 6*r # 방이 한번에 6*r개 씩증가,
    r += 1 # 이 때 r은 1개씩 증가

# 출력: 거리 출력
print(r)


