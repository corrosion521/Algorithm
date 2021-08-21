'''
m이상 n이하 소수 모두 출력
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
#입력: m,n
m,n = map(int,input().split())

#계산 : m~n범위내의 소수 전부 출력
for i in range(m,n+1):
    if sosu(i)==True:
        print(i)


'''
1. for - range안 소수 ㄴㄴ 
2. 소수 구할 때 그 수의 제곱근까지만 구해도 소수판별됨.-이걸 어케 알아
'''



