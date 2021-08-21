'''
소인수분해
2이상으로 나누는데,
2가 안되면 그 이상 최소값으로 계속해서 나눠감
나눈 몫을 계속 그 최소값으로 나누는 것.
'''

#입력 :1<=n<10 000 000
n = int(input())

#계산: 1남으면 끝
while n!=1:
    for i in range(2,n+1):#인수 찾기
        if n%i==0:
            insu = i
            break
    print(insu)#출력 : 인수
    n //=insu#계속 나눠가자


