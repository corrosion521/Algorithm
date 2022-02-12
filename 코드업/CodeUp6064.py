'''
괄호, 부호에 따른
우선순위가 있다는 점을
이용하자.
특히 괄호를 잘 이용해보자.
'''
a,b,c = map(int,input().split())

print(a if(a<=(b if(b<=c) else c)) else (b if(b<=c) else c))
