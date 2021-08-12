#입력 : 테스트 케이스
t = int(input())

#입력,계산 : h,w,n 후 n에 맞춰 line,room 계산. 흐름 파악하여 예외처리
for i in range(t):
    h, w, n = map(int, input().split())

    line = n % h # 줄(층)
    room = n // h + 1 # 칸

    if line == 0:#예외 케이스 - 칸 하나내리고, 라인은 full로
        room -= 1
        line = h
    # 출력 : 방번호
    print(line * 100 + room)

