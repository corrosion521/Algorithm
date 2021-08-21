'''
m이상, n이하의 자연수중 소수인 것을 골라, 이들의합, 그리고 이들 중 최소값은?
'''
#함수 : 소수판별
def sosu(a):
    count = 0
    if a ==1:
        return False
    for i in range(1,a):
        if a%i==0:
            count+=1
    if count==1:
        return True
    else:
        return False

#입력:m
m = int(input())

#입력:n
n = int(input())

#계산: 소수판별 후 합 ,최소값 찾기
sum = 0
count = 0 #최소값 저장용
for i in range(m,n+1):
    if sosu(i)==False:#소수아니면 아래 통과
        continue
    if count==0 and sosu(i)==True:#최소값 첫 지정
        min = i
        count+=1
    else:#최소값 첫 지정 후에는 여기를 통해 최소값 찾아줌.
        if min>i:
            min=i
    sum+=i

#출력:소수의 합, 최소값
if sum ==0 :
    print("-1")
else:
    print(sum)
    print(min)


