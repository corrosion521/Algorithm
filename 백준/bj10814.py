'''
1. 당연하지만 리스트 안에 리스트(2중 리스트) 를 염두해두자. 한 리스트안에 두 가지 이상을
사용하고자 할 경우. 물론 dict가 좋지만, key 중복을 사용하기 어렵다는 점이 있다.
2. 항상 문자와 숫자를 잘 구별해보자
'''
import sys

N = int(sys.stdin.readline()) # 회원수
member = []

for i in range(N):
  member.append(list(sys.stdin.readline().split()))

member.sort(key=lambda x:int(x[0]))

for i in range(N):
  print(member[i][0]+" "+ member[i][1])