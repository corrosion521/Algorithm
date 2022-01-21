#입력 : 영문 소문자 1개
al = input()

#출력 : a~입력까지의 알파벳 출력
for i in range(ord('a'),ord(al)+1):
    print(chr(i),end=' ')


'''
숫자 뿐 아니라
문자도 대소비교 가능함(아스키 코드)

'''
'''
c = input()
k = 'a'
while c>=k:
    print(k,end=' ')
    k=chr(ord(k)+1)
'''