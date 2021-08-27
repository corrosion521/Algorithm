'''
프랙탈 생성..
입력 n
nxn 생성
초기형태
***
* *
***
그 이후도 중앙 부분은 구멍 뚫림
'''

#함수 : 프랙탈 증가 (3배수)
def fra(list):
    k = len(list)
    list2=[]
    for i in range(k*3):# 행
        if i//k == 1:# 빈칸 만들기(행조절) , 초기리스트는 그냥 뚫어져 있지만(* *) 이후로는 따로 뚫어줘야됨.
                     # 그게 i//k인 것. 이게 작동되는 건 한번씩임. 커졌을때 나오는 다른 빈칸들은 이미 그전에 생성된 것들.
                     # k가 3일떄는 3~5 9일떄는 9~17...
            list2.append(list[i%k]+' '*k+list[i%k])# *k인 이유: 규칙성으로 알아봐도 좋고, 이 전 프랙탈의 열의 길이이기도 하다.
        else:
            list2.append(list[i%k]*3)#열
    return list2

#초기 리스트
list = ["***","* *","***"]

#입력 : n
n = int(input())

#계산 : 지수 구하기
count=0
while True:
    if n == 3:
        break
    n//=3
    count+=1


#계산 : 재귀
for i in range(count):
    list=fra(list)


#출력 : list, 한 행씩 출력하여 결과물을 도출해냄.
for i in list:
    print(i)


'''
알고리즘 기초
1.디버그프린트
2.표본 실행
3.실제움직임 != 구현 일 수도 있음(예를 들면 여기서는 한 줄 씩 )

재귀함수
1. 형식에 얽매이지 말기
2. 함수안의 함수를 호출한다는 점만 주의.
'''