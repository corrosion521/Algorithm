n = int(input())

list = list(map(int,input().split()))# 입력 리스트
result=[0]*23# 기록 리스트

#기록- 기록리스트
for i in range(n):
        result[list[i]-1]+=1

#기록리스트 출력
for i in range(23):
    print(result[i],end=' ')


