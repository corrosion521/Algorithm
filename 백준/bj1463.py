'''
dp
1. 전의 결과를 다음 결과에 이용..
=> 재지정에서 많이 사용됨.
2. dp의 값이 무엇인지 잘 생각해보기
'''


def make_1(n):
    dp = [0] * (n + 1)  # dp생성

    for i in range(2, n+1):
        dp[i] = dp[i - 1] + 1  # 3. 1빼면 카운트 하나 올라가므로

        if i % 3 == 0:  # 1. 3으로 나누어 떨어지는 경우
            dp[i] = min(dp[i], dp[i // 3] + 1)  # 재지정- 3(1뺴기만 적용) vs 1

        if i % 2 == 0:  # 2. 2으로 나누어 떨어지는 경우
            dp[i] = min(dp[i], dp[i // 2] + 1)  # 재지정- 3(1빼기만 적용) vs 2

    return dp[n]

print(make_1(int(input())))