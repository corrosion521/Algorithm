#오답
#계산- 함수 : 손익분기점(Break-EVEN-point)나는 판매량.
def bep(a,b,c):
    n = 0
    i = 0
    while c*i<=2100000000 :
        if c*i>a+b*i :
            return i
        i+=1
    return -1


#입력 : A - 고정 비용,B - 가변 비용,C - 노트북 가격/(21억 이하)
A,B,C = map(int,input().split())


#출력 : 손익분기점의 판매량
n = bep(A,B,C)
print(n)