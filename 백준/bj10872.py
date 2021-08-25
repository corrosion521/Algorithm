'''
N! 출력하기
'''
def multiply(n):
    a=0
    if n>0:
        return n * multiply(n - 1)
    elif n==1:
        return n
    else:
        return 1
#입력 : 0<=n<=12
n = int(input())

#계산,출력
print(multiply(n))
