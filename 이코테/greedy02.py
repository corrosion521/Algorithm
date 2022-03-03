'''
idea
1. greedy
1) 기준 : +,x 연산
1> 0,1은 무조건 더하기. 0이 아닐때까지는 더하기
2> 나머지는 x

learn
1. 매번 강조하지만 알고리즘은 worst case파악이 매우 중요하다
'''

s = input()
result = int(s[0])# 첫 글자, 결과값

for i in range(1,len(s)): # 두 번째 글자부터 s 탐색
    if result<=1 or int(s[i]) <=1: # 결과값이 1이하, 혹은 연산값이 1이하면 더하기
        result += int(s[i])
    else: # 그 이외네는 곱하기
        result *= int(s[i])

print(result)
