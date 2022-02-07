'''
1. str(숫자) : 숫자 -> 문자
2. int(문자열) : 문자열 -> 숫자
명심하자.
'''

N = int(input()) # 분해합 입력

plus=0 # 생성자의 부품(각 자리수의 합), 부품+후보 == 생성자

for i in range(N+1): # 0부터 분해합(N)까지를 후보로 침
    plus=0 # 부품 초기화
    i=str(i) # 생성자 부품 제작 위해 str화 시켜 리스트로 이용
    for j in range(len(i)):# 숫자 자리수만큼 다 더해 부품제작
        plus +=int(i[j]) # 생성자 부품 제작 완료
    if plus + int(i)== N: # 만일 생성자 부품+생성자 후보 == 분해합 이면 break
        break

if N==int(i): #생성자 없는 경우.(for문 다돌고 나옴)
    print("0")
else:
    print(i)# 출력

