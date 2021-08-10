#입력 : 월(1~12)
a = int(input())

#계산 ,출력 : 계절이름
if a//3==1:
    print("spring")
elif a//3==2:
    print("summer")
elif a//3==3:
    print("fall")
else :
    print("winter")



