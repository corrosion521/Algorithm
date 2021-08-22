'''
골드바흐의 추측: 2보다 큰 모든 짝수는 두 소수의 합으로 표현가능
ex)
4 = 2+2, 6 = 3+3(좌변의 수: 골드바흐 수 , 여기서 이렇게 합으로 표현하는 것 : 골드바흐 파티션)
'''

#함수 : 소수 판별
def sosu(a):
    if a==1:
        return False
    else:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return False
        return True
#소수 리스트 생성
list=[]#소수리스트
for i in range(2,10001):
    if sosu(i)==True:
        list.append(i)

#골드 바흐 파티션 함수
def gold(n):
    a=list[0]
    for i in list:#소수중
        x = a #새로운 파티션 원소의 직전 보관, 혹시나 새로운파티션(a)가 두 조건을 충족시키지 못할 것 대비
        a = i# 첫 번째 파티션원소 지정
        if n - a not in list:#조건1: 두 번째 원소가 소수여야됨. 이를 성립시키지 못하는 걸 거르기위한 조건
           a = x# 조건 충족 안되서 보관되있던걸 다시 a로
           continue
        if a > n - a:#조건2: 두 번째 원소는 소수가 맞다만(첫번째 조건 충족),첫원소>두번째원소 기에 보관되있던(직전의 파티션)을 출력한다.
                return print(x, n - x)
        elif a == n - a:#조건2-2: 첫 번째 원소==두 번째 원소면은 그냥 지금 있는거 그대로(a,n-a)출력.
            return print(a,n-a)

#입력:t(testcase), 4<=n<=10000
t = int(input())
for i in range(t):
    n = int(input())
    gold(n)

'''
pypy3로만 되네.. 
'''