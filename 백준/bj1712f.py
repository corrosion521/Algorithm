#계산- 함수 : 손익분기점(Break-EVEN-point)나는 판매량.
def bep(a,b,c):
        if b>=c :
            return -1
        else:
            return a//(c-b)+1

#입력 : A - 고정 비용,B - 가변 비용,C - 노트북 가격/(21억 이하)
A,B,C = map(int,input().split())

#출력 : 손익분기점의 판매량
n = bep(A,B,C)
print(n)