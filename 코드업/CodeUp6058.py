#입력 : 정수 두개
a,b = map(int,input().split())

#계산 및 출력: 두 불값이 모두 False일 때만 True
print(not bool(a) and not bool(b))