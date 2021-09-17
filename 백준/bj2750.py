'''
1. 지정반복문(맨오른쪽 원소제외),비교반복문 설정.
2. 최소인덱스 초기지정
3. 최대 원소를 찾는다
4. 최대 원소와 맨 오른쪽 원소를 교환한다
'''

def sel(list):
    for i in range(len(list)-1):#마지막 까지 안가는 이유. 마지막은 자동정렬됨.
        min_index = i

        for j in range(i+1,len(list)):
            if list[j]<list[min_index]:
                min_index = j
        list[i],list[min_index] = list[min_index],list[i]

N = int(input())
list = []
for i in range(N):
    list.append(int(input()))
sel(list)

for i in range(N):
    print(list[i])
