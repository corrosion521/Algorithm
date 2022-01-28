'''
1. 런타임 에러- 반복 등 구조 점검(시간복잡도 줄이기). 안된다 싶으면 다른 방법
2. max(), 리스트.index(값)  함수
'''
list=[]

for i in range(9):
     list.append(int(input()))

print(max(list))
print(list.index(max(list))+1)