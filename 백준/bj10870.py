'''
피보나치 수열
0 1 1 2 3 5...
'''


# 함수: 재귀 피보나치
def fibo(n):
    if n<=1:# fibo (0),(1) 일 때 break를 걸어줌.
        return n
    return fibo(n-1)+fibo(n-2)



#입력:n
n = int(input())
#출력:피보나치
print(fibo(n))


'''
1. for 문 사용
# 입력 : 0<=n<20
n = int(input())
list =[]
list.append(0)#0번째
list.append(1)#1번째

# 계산 : 피보나치 수열
for i in range(n-1):# c의 번호 : 2번째~10번째
    c = list[i]+list[i+1]
    list.append(c)

# 출력
print(list[n])#n번째


2. 재귀함수 
  1)return 함수 가 point
  2)if 등의 조건문을 통한 break를 걸어줘야함 (무한 반복하면 안되기에) 
'''
