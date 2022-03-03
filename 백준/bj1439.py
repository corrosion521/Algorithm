'''
idea
1. greedy
1) 기준: 0-1뒤집기. 0,1중 최소 연속 부분을 골라 출력

learn
1. 조건문의 break 시점을 잘 파악하자.
'''

s = input()

a = 0  # 0집합 개수
b = 0  # 1 집합 개수
for i in range(1, len(s)):  # 두번째 부터 검사 (out of range고려)
    if s[i] == '1':  # 1일 경우
        if (s[i - 1] == '0'):  # 전이 0이면
            a += 1  # 0집합 마치고 나왔으므로 a count up
        if i == (len(s) - 1):  # 마지막이면 마치고 나왔다고 쳐서
            b += 1  # 해당(1) 증가

    # 같은 케이스
    if s[i] == '0':
        if (s[i - 1] == '1'):
            b += 1
        if i == (len(s) - 1):
            a += 1

print(min(a, b))  # 적은 수의 집합 수만큼 뒤집으면 됨
