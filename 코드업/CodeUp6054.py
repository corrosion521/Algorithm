'''
논리 연산자는
" 논리식(true or false)를 판단하여"
true false 를 반환하는 연산자.

결국 처음부터 끝까지 true false로 이루어짐.

비교연산자는 true false를 반환할 뿐
'''
a,b = map(int,input().split())
print(bool(a) and bool(b))