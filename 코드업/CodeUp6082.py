'''
문제조건 똑바로 읽기.
기본이다.
괜히 제대로 안읽으면 훨씬 어렵게 풀게됨.

조건 식이 너무 어렵다 싶으면
if와 else의 전환을 떠올려보자.
'''
'''
n = int(input())

for i in range(1,n+1):
        if (i%10)%3!=0:
            print(i,end=' ')
        elif i%10==0:
            print(i,end=' ')
        else:
            print("X",end=' ')
'''
a = int(input())

for i in range(1,a+1):
    if(i%10==3 or i%10==6 or i%10==9):
        print('X ',end='')
    else:
        print('%d '%i,end='')