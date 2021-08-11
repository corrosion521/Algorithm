# 입력 : 분수의 위치
X = int(input())

# 규칙 : 첫 번째 라인 개수 1,두번쨰 개수2,세번째라인 개수 3...
# 개수를 늘리며 라인을 찾음 그 후 그 라인 상의 분수를 찾음

# 계산 : 라인 찾기

#초기값
a=1#분자
b=1#분모
line = 1 #라인,초기 값은 라인1, 라인번호 == 라인안의 분수들의 개수
linei = 1 #라인 내의 위치. 라인이 짝수인지 홀수인지에 따라 마지막이 될수도,처음이 될수도있다.

#X의 위치보다 linef가 더 클때 break. 이를 통해 X의 라인을 찾음
while True:
    linei += line
    line+=1

    if linei>X:
        break

#계산: 라인찾기 - 넘어 갔으니 복구
line -=1
linei -= line

#계산: 라인 내에서 분수의 위치찾기
if line%2==0:#지그재그기에 라인의 짝,홀수에 따라 라인 내 위치,증감이 다름
    b = line
    for i in range(linei, X):
        a += 1
        b -= 1
else:
    a = line
    for i in range(linei, X):
        b += 1
        a -= 1

#출력 : 분수
print(a,"/",b,sep="")


