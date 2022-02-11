'''
1. sort는 정렬함수. 문자까지도 정렬해준다. key값(+람다식)이용하여 정렬,다중정렬 가능
2. set함수 (집합,중복 허용x,순서x) 잊지 말자. 또 집합으로 변환해주는 것이기 때문에, list화 시켜야한다.
   - { 1, 2,3, 4, ~~}(set)형식으로 출력. tuple은 소괄호( ( ) ) 니 착각 x
   리스트,튜플,세트,딕셔너리의 차이 알기.
+
for i in range(N): # N줄에 걸쳐서 알파벳 소문자 단어가 입력됨
    k = input()
    if k in wlist:
        wlist.pop()
    else:
        wlist.append(k)
        나는 처음에 이런식으로 조건문과 pop을 통해 중복제거 하고 입력했다.

3. sys.stdin.readline() : input()뽀다 빠른 입력, sys import하자
   다만 개행까지 입력되므로 strip()을 이용하여 공백을 제거하자(strip은 양옆공백 모두 제거)
'''
import sys

N = int(sys.stdin.readline()) # 단어 개수 입력

wlist=[] # 단어장

for i in range(N): # N줄에 걸쳐서 알파벳 소문자 단어가 입력됨
    wlist.append(sys.stdin.readline().strip())

# set을 활용하여 단어장의 중복 제거
wlist =list(set(wlist))

# 정렬기준 len,사전순 lambda식 이용하여 키값(기준) 지정
wlist.sort(key=lambda x:(len(x),x))

# 단어장 출력
for i in range(len(wlist)):
    print(wlist[i])