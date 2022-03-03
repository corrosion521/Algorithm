'''
idea
1. greedy
1) 1원부터 시작, 가장 적은 금액(주어진 동전들로는 만들 수 없는)

learn
1. itertools의 combinations로 조합 사용
2. combinations(리스트(범위), 선택 값의 수 )
3. 문제에 주어진 조건들을 "모두" 조합하여 하나의 흐름을 만들어보자.
조건 한 두가지를 소홀하게 여겨서 돌아가는 경우가 많다
ex) 1원이 없으면 사실상 계산이 성립이 안됨 = > 1원이 필수 => 해당 코인 까지 1차이나는 금액을 만들어낼 수 있음
'''

# 내가 푼 코드. 흐름파악이 부족하여 전부 구현했기에 메모리 사용이 비효율적임.

# from itertools import combinations
# 
# n = int(input())
# 
# l1 = list(map(int, input().split())) # 본 리스트
# 
# l1.sort() #정렬.
# 
# # 조합 생성
# l2 = []
# for i in range(n + 1):
#     l2 += list(combinations(l1, i))
# 
# # 조합 튜플들의 합들을 리스트에 넣음
# l3 = []
# for i in range(len(l2)):
#     l3.append(sum(l2[i]))
# 
# # 중복 제거
# l4 = list(set(l3))
# 
# if min(l1) > 1:# 1원이 없으면 만들 수 없는 금액의 최소는 1이됨
#     print("1")
# else: # 그 외는
#     for i in range(1, len(l4) - 1): # 조합 공집합 고려 1부터 조합리스트 다 뒤짐
#         if l4[i] + 1 != l4[i + 1]: # 조합 리스트 중 오름차순이 끊기면
#             print(l4[i] + 1) # 끊긴부분 + 1
#             break # 탈출
# 
#         if i == len(l4) - 2: # 이 경우는 조합 리스트가 끊기지 않고 빼곡히 오름차순일때
#             print(l4[i + 1] + 1) # 조합리스트의 최대값보다 1큰수가 만들 수 없는 금액이 된다.

# 답안
n = int(input())

l1 = list(map(int,input().split())) # 리스트 입력
l1.sort() # 정렬(작은 단위부터 더하기 위해)

result = 1 # 최소값 디폴트

for coin in l1: # 동전 하나 씩 올려가며

    if result<coin:# 현재 코인으로 만들어진 것+1(디폴트가 1이기에)보다 coin이 클 경우
        # 중요! 1짜리 코인이 있어서 해당 코인 전까지 1차이나는 금액을 만들어 낼 수 있음을 유의
        break # break
    result+=coin
print(result)  # 현 코인 금액+1 (result) 보다 coin이 크다는 건 그 사이에 틈이 있음을 말하는 것
