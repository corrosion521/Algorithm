'''
print()에는 end='\n'가 디폴트라는 점 유의
'''

s = input()

for i in range(3):
    print(s[i*2]+s[i*2+1],end=' ')

#print(s[0:2],s[2:4],s[4:6],sep=' ')도 있다.