'''
1.&(교집합) :  파이썬에서 &는 쓰이지 않는 것이 아니었다.
2. set() 은 []첨자 scriptable 사용 불가능하다.
3. list()로 set()도 리스트화 시킬 수 있다.
반대로 set()도 리스트를 집합화 시킬 수 있다.
set() < - > list()
'''


n,m = map(int,input().split())
l1=[]
a = set()
for i in range(n):
     a.add(input())

b = set()
for i in range(m):
    b.add(input())

c = a&b

# for i in c:
#     l1.append(i)
l1 = list(c)

l1.sort()
print(len(l1))
for i in range(len(l1)):
    print(l1[i])