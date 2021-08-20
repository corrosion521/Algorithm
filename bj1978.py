'''
n개의 수 중 소수가 몇개 인지 출력
소수라는건 약수가 자신과, 1밖에 없는 수.(1보다 커야됨)
역시 하나씩 다돌려봐야 되나..
1부터 자신까지 %나머지를 조사해서 0인경우 count
count가 2가 아니면 소수가아니다

'''

#입력:(test case) n>=100
n = int(input())
#입력: n개의 수 n>=1000
list = list(map(int,input().split()))

# 계산 : 한 개 씩 소수인지 아닌지 count하여 판별
result = 0# 소수의 개수
for i in range(len(list)):#list 다 검사
    count = 0#나누어떨어지는 수의 개수
    if list[i]>1:#list[i]가 1보다 클 경우(소수 조건1)
        for j in range(1,list[i]+1):#소수 count 검사(소수조건2)
            if list[i] %j==0:
                count+=1
    if count==2:
        result+=1

# 출력 : 결과
print(result)
