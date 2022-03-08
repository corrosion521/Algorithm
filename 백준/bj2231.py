'''
1. str(숫자) : 숫자 -> 문자
2. int(문자열) : 문자열 -> 숫자
명심하자.
'''
# 과거 코드
# N = int(input()) # 분해합 입력
#
# plus=0 # 생성자의 부품(각 자리수의 합), 부품+후보 == 생성자
#
# for i in range(N+1): # 0부터 분해합(N)까지를 후보로 침
#     plus=0 # 부품 초기화
#     i=str(i) # 생성자 부품 제작 위해 str화 시켜 리스트로 이용
#     for j in range(len(i)):# 숫자 자리수만큼 다 더해 부품제작
#         plus +=int(i[j]) # 생성자 부품 제작 완료
#     if plus + int(i)== N: # 만일 생성자 부품+생성자 후보 == 분해합 이면 break
#         break
#
# if N==int(i): #생성자 없는 경우.(for문 다돌고 나옴)
#     print("0")
# else:
#     print(i)# 출력

'''
idea
1. 생성자는 없을수도, 1개일 수도 다수일 수도  있다
2. 한 자연수의 가장 작은 생성자는?
3. n보다 낮은 수, 1부터 다 돌려보기?

learn
1. str(숫자) : 숫자 -> 문자
2. int(문자열) : 문자열 -> 숫자
'''
n = int(input())

final=0 #최종값, 생성자 없으면 0
for i in range(n,0,-1): # n으로 부터 내려가며 탐색
  result = i # 우선 생성자 후보 저장 ,result는 생성자 여부확인의 변수
  i = str(i) # 각 자리수 더하기 위해 string화
  for j in i: # 한 자리수 씩 탐색
    result+=int(j) # 하여 결과 값에 더하기
  if result ==n: #만일 i가 생성자면?
     final=i#저장

print(final)