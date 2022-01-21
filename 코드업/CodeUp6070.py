'''
m = int(input())

if m>=3 and m<=5:
    print("spring")
elif m>=6 and m<=8:
    print("summer")
elif m>=9 and m<=11:
    print("fall")
else:
    print("winter")
'''

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




