
'''
그냥 문자->숫자 + 십육진수 값(+10) 이용
c = input()
c=ord(c)-ord('A')+10
for i in range(1,16):
    print("%X*%X=%X"%(c,i,c*i))
'''
'''
16진수 변환 함수
int(?,16)

'''
c = int(input(),16)
for i in range(1,16):
    print("%X*%X=%X"%(c,i,c*i))