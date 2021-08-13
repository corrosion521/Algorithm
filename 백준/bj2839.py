# 배달 n, 5,3이용해서 최소한의 봉지를 이용하는 방법?

# 입력 : n
n = int(input())

# 계산: 5 3 이용
result = 0
while True:# 딱 안떨어지면 반복문 탈출됨
    if n % 5 ==0:# 5짜리만으로 해결 가능
        result = result + n//5
        print(result)
        break

    # 5안되면 3으로 하나씩 빼주기
    n-=3
    result  +=1

    if n<0: #애초에 입력잘못,딱 안떨어지는 경우
     print("-1")
     break



