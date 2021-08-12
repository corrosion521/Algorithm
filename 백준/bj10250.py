# 규칙 " 정문 거리순 배정 : 동일시 H(층) 낮은 순 배정

# 입력 : T(데이터 수),H(호텔 층수),W(각 층 방수),N(몇 번 째 손님인지)
t = int(input())
for i in range(t):
    h,w,n= map(int,input().split())

    # 계산 : 이중리스트 생성하여 방번호 넣기
    rn = 101 #디폴트 방번호
    room=[]
    for j in range(h):
        line =[]
        for i in range(w):
            line.append(rn + i)
        rn = 100 * (j + 2) + 1
        room.append(line)

    # 계산 : 손님에게 방 배정

    a = n//h + 1
    l = n%h # % 개념 숙지

    if l ==0: # 예외처리
        a-=1
        l =h

    # 출력 : 방 번호
    print(room[l-1][a-1])#인덱스이므로 1씩 낮춤










