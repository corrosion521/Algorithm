'''
idea
1. greedy
1) 기준. 채워야할 값보단 아래인 화폐단위중, 최대값부터  가능한 한 선택하여 채울 값을 줄여나가기
2) 정렬. 화폐값 .큰 값부터 ~작은값
'''

import sys

n, k = map(int, input().split())
coins = []  # 동전 종류
count = 0  # 동전 개수

for i in range(n):
    coins.append(int(sys.stdin.readline().strip()))

coins.sort(reverse=True)#내림차순(큰 순서)로 정렬


for x in coins:# 동전 종류 별 탐색
    if x<=k:
        tmp=k//x
        count+=tmp
        k-=tmp*x


print(count)