T = int(input()) # 테스트 케이스 수

for i in range(T):
    n=1
    H, W, N = map(int, input().split())  # 호텔 층수, 각 층 방수, 몇 번째 손님?
    while N>H:
            N = N-H
            n+=1
    print(N,"%02d"%n,sep="")