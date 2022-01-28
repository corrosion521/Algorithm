# 테스트 케이스 횟수 입력
T = int(input())

# 테스트 케이스 입력(T회)
for i in range(T):
    R,S=input().split() # R회 반복, S문자열 입력
    R=int(R) # R 정수화

    # ?회차 출력
    for i in range(len(S)):
        print(S[i]*R,end="")
    print()# ?회차 출력 후 개행