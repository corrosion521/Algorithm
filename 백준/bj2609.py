'''
1. 유클리드 호제법 : GCD(최대공약수)를 쉽게 구할 수 있음.
1) a,b(a>b), a와 b의 GCD인 G는 b와 a%b의 GCD인 G'와 같다
ex) gcd(24,18) = gcd(18,6) =gcd(6,0) . b가 0이되는 순간의 6이 최대공약수.
2) 최대공배수 : A로 나눠도 ,B로 나눠도 떨어지는 수중에 가장 작은 수
== A*B/gcd(a/b) -- (A*B안에 최대공약수가 2개(A에 하나 , B에 하나)들어가있음을 염두, 따라서 gcd로 나누는거 )
2. 재귀함수: 반환(return)에 유의할 것. return 있고 없고 차이가 크다.
3. swap: ex) a,b= b,a 딱히 순서가 없음. 동시에 바꾼다고 생각하면 됨.
'''

import sys
# 최대공약수
def gcd(a,b):
    while b!=0:
        a,b= b,a%b
    return a

# 최대공약수 - 재귀
def gcd_r(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

# 최소공배수
def lcm(a,b):
    return a*b//gcd(a,b)

# 입력
a,b = map(int, sys.stdin.readline().split())

# 대,소 순으로 swap
if a<b:
    a,b= b,a

#출력
print(gcd_r(a,b))
print(lcm(a,b))
