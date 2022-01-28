# 테스트 케이스의 개수 입력
n = int(input())


for i in range(n):
    result = 0  # 최종 점수
    s = input() # 채점 한 회 입력
    score = 1 # 정답(O) 시 배점 초기값
    for i in range(len(s)): # 채점 (한 회)
        if s[i]=='O': # 정답 일 경우
            result+=score # 최종 점수에 배점 등록
            score+=1 # 우선 배점 하나 올려줌
        else: # 오답일 경우
            score=1 # 오답일 경우 배점은 1점으로 다시 초기화

    print(result) # 채점 한 회분 출력