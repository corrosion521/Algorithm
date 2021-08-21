'''
베르트랑 공준-
n에 대해 n<=x<=2n 범위에서 소수 x가 적어도 하나 존재한다.
자연수 n이 주어졌을 때 n~2n의 소수의 개수?
'''
#함수 : 소수 판별
def sosu(a):
    if a==1:
        return False
    else:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return False
        return True

#입력: n,계산:범위 내 소수의 개수
n=111
# 미리 소수 담아버리기
list=[]#소수리스트
for i in range(2,246912):
    if sosu(i)==True:
        list.append(i)

#출력: 케이스별로, list처음부터 다돌려서 범위내의 수(n~) 만 카운트해봄
while True:
    n = int(input())
    if n==0:
        break
    count = 0
    for i in list:
        if n<i<=n*2:
            count+=1
    print(count)#출력
'''
본래의 시간 복잡도: O(n*(n**0.5))=O(n^2)=>
이 때는 매 케이스마다 소수판별을 해줘야 됬음

while True:
    n = int(input())
    if n==0:
        break
    count = 0
    for i in range(n,2*n+1): !!! 매 케이스 마다 소수판별
        if sosu(i)==True: !!!
            count+=1
    print(count)#출력
    
수정 후 : O(246912+246912)

결론: 추가작업이 필요했지만, 불필요한 반복작업을 줄여서 시간을 단축시켰다(-: 소수판별, + 리스트생성)

'''