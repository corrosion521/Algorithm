'''
idea
1. greedy
1) 무게가 다른 볼링공 쌍 조합 들
2) dict써서 번호:무게 - 사실 인덱스가 순차적이라 번호를 따로 기록할 필요가 없었다.
3) 무게 같은 경우만 쌍 생기도록 조정

learn
1.하나의 반복문 + 변수의 조합으로 여러 변화를 가져옴
1) 무게리스트의 변화로 인한 n의 변화
2) 그 변화를 이용하여 result도 변화
'''

# 정답이기는 하나, 이중 for문은 메모리 사용이 커서 되도록 피하는게 좋으니 답안을 적었다.
# n,m = map(int,input().split()) # 개수, 무게 종류 수 입력
# k = list(map(int,input().split())) # 번호(인덱스) 무게 리스트 입력
#
# # 인덱스 0부터 시작인 것 고려(-1) DICT에 무게-
# # d1={} # 볼링 dict로 저장 -   번호: 무게
# count = 0 # count
# # for i in range(n):# 볼링공 개수만큼
# #     d1[i] = k[i] # dict에 번호에 맞게 정보(무게) 저장 해준다.
#
# # 중복음 염려 (i-j)하여 탐색
# for i in range(n):
#     for j in range(i+1,n): # 해당 고정(i)보다 뒤
#         if k[i]!=k[j]: # 무게가 다를 경우는 선택 가지수 count up
#             count+=1
#
# print(count)

n, m = map(int, input().split())  # 개수, 무게 종류 수 입력
k = list(map(int, input().split()))  # 번호(인덱스) 무게 리스트 입력

l1 = [0] * 11  # 0은 제외 무게 리스트

# 무게 리스트 채우기
for i in k:
    l1[i] += 1

result = 0

# 하나의 반복문 + 변수의 조합으로 여러 변화를 가져옴 : 1) 무게리스트의 변화로 인한 n의 변화->2) 그 변화를 이용하여 result도 변화
for i in range(1, m + 1):
    n -= l1[i]  # 무게 리스트 돌면서 있으면 볼링공 개수 빼버림( 무게리스트의 1들 합 == 볼링공 개수)
    result += l1[i] * n  # 해당 무게 볼링공 개수  * B가 선택하는 경우의 수 (n)

print(result)
