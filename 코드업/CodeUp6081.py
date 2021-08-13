#입력: A~F, 단
dan = input()

#출력: 16진수 구구단

for i in range(1,16):
    print(dan,"*","%X"%(i),"=","%X"%(int(dan,16)*i),sep="")