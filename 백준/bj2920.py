''' 방법 1 - 내장함수 이용 x
# 숫자(음) 입력
d=[]
d=list(map(int,input().split()))

stka=0 #어센딩 스택 7되면 출력
stkd=0 #디센딩 스택 7되면 출력

#0-1 ~ 7~8까지 비교해나가기
for i in range(1,8):
    if d[0]==1:# ascending 후보
        if d[i-1]+1==d[i]:
            stka +=1
    elif d[0]==8:#descending 후보
        if d[i-1]-1==d[i]:
            stkd += 1
    else: # 불순물 하나라도 있으면 바로 mixed
        print("mixed")
        break

if stka == 7 :
   print("ascending")
if stkd == 7 :
    print("descending")
'''

'''
방법2. sorted 내장함수 사용
'''

d=[]
d=list(map(int,input().split()))


if d ==sorted(d):
    print("ascending")
elif d == sorted(d,reverse=True):
    print("descending")
else:
    print("mixed")