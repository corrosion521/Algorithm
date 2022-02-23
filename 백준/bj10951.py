'''
1. try~except 구문:
1)
try: ~
except: ~
2) 무한 반복문 시 입력이 안되는 경우를 에러처리 시켜줘야함.

'''
while True:
    try:
        A,B= map(int,input().split())
        print(A+B)
    except:
        break