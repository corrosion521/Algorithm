'''
직각 삼각형 판별?
여러 test case, 마지막은 0 0 0
'''

# 입출력+계산
while True:
    result= list(map(int,input().split()))
    c = max(result)
    result.remove(c)
    a = result[0]
    b = result[1]
    if a==0 and b==0 and c==0:
        break
    if a**2+b**2==c**2:
        print("right")

    else:
        print("wrong")

'''
조건 주의 하자.. 예시가 다가 아님
예시는 일부에 불과하다...

'''