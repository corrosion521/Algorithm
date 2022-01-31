'''
1. TypeError: 'int' object is not callable
=> 예약어를 변수명으로 사용하면 이렇게 됨
ex) max 를 변수명
'''
while True:
    a = list(map(int,input().split()))
    m = max(a)
    a.remove(m)

    if a[0] ==0 and a[1]==0 and m==0:# 브레이크
        break
    if a[0]**2 + a[1]**2  == m**2: # 계산
        print("right")
    else:
        print("wrong")