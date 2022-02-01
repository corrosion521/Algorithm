
while True:
    a = input()
    b = 0 #팰린드롬 검사 여부 , -1이면 x 0이면 O 
    if len(a) == 1 and a[0] == '0': # 0입력시 탈출
        break

    for i in range(len(a)//2): # 짝수 시 반, 홀수시 중간까지
        if a[i] != a[len(a)-1-i]: # 앞 뒤 검사
            print("no")
            b = -1 # 팰린드롬 아님
            break

    if b == 0: # 팰린드롬
        print("yes")




