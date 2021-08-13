# 규칙
'''
3층 1
2층 1 4 10 ...
1층 1 3 6 10 15 21
0층 1 2 3 4 5 6

규칙성 - 층의 호실 사람수 변경(층 상승시, 그려보면 같은층 전 호수+아래층 같은 호수=층값)
'''

# 입력: 테스트 케이스,층,호수
t = int(input())
for _ in range(t):
    floor = int(input()) #층
    room = int(input()) #호수

    # 0층 만들어 놓고 목표의 층까지 수를 늘려나감
    flr_0 =[x for x in range(1,room+1)] # 0층의 리스트 : 1~room
    for i in range (floor): #층 반복
        for j in range(1,room): #호수 반복
            flr_0[j]+=flr_0[j-1] #층의 호실 사람수 변경(층 상승시, 그려보면 같은층 전 호수+아래층 같은 호수=층값)
    print(flr_0[-1])#-이용하여 목표 층수 뽑아냄(최대값)

