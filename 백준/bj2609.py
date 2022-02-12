'''
1. 유클리드 호제법 : GCD(최대공약수)를 쉽게 구할 수 있음.
1) a,b(a>b), a와 b의 GCD인 G는 b와 a%b의 GCD인 G'와 같다
ex) gcd(24,18) = gcd(18,6) =gcd(6,0) . b가 0이되는 순간의 6이 최대공약수.
2) 최대공배수 : A로 나눠도 ,B로 나눠도 떨어지는 수중에 가장 작은 수
== A*B/gcd(a/b) -- (A*B안에 최대공약수가 2개(A에 하나 , B에 하나)들어가있음을 염두, 따라서 gcd로 나누는거 )
2. 재귀함수: 호출 후 return시 불러낸 함수로 돌아간다는 점 명심할 것. 최초의 함수로 return하는게 아님!
3. swap: ex) a,b= b,a 딱히 순서가 없음. 동시에 바꾼다고 생각하면 됨.
'''

import sys

def gcd(a,b):
    while b!=0:
        a,b= b,a%b
    return a

def lcm(a,b):
    return a*b/gcd(a,b)

a,b = map(int, sys.stdin.readline().split())

if a<b:
    a,b= b,a

print(gcd(a,b))
print(int(lcm(a,b)))
