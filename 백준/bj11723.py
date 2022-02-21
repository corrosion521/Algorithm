'''
1. set() 리스트,딕셔너리,셋,튜플 중 하나인 셋. 집합.
당연하지만 리스트로 다시쓰려면 list()써줘야함.
또 se = {} 이건 dict임 . 주의 할 것. set()으로 해줘야함.
1) remove(원소) : 특정 원소 삭제. 인덱스 아님.
2) clear(): 리스트 내용 모두 삭제
3) add(원소 ) :특정 원소 추가, 리스트와의 차이점

2. range(?,?): 정수의 범위 임을 명심. '1' 과 1의 차이를 유념하자.
'''

import sys

m = int(input()) # 연산 수
rst=set() # 집합
li=[] # 입력 명령

for i in range(m):
    li= sys.stdin.readline().split()

    if len(li) == 2: # all 명령 시 생성되는 range값들이 정수인 것을 고려, 입력 값을 int로 변환시켜 준다.
       li[1] =int(li[1])

    if li[0] == "add":
            rst.add(li[1])

    elif li[0] == "remove":
        if li[1] in rst:
            rst.remove(li[1])

    elif li[0] == "check":
        if li[1] in rst:
            print("1")
        else:
            print("0")

    elif li[0] == "all":
        rst = set(range(1,21))

    elif li[0] == "toggle":
        if li[1] in rst:
            rst.remove(li[1])
        else:
            rst.add(li[1])

    elif li[0] == "empty":
            rst.clear()
