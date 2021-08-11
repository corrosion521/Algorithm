#입력 : 영문 소문자 1개
al = input()

#출력 : a~입력까지의 알파벳 출력
for i in range(ord('a'),ord(al)+1):
    print(chr(i),end=' ',)