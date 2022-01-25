def seq1(a,m,d):
    return (a*m)+d

a,m,d,n= map(int,input().split())

for i in range(n-1):
    result=seq1(a,m,d)
    a = result

print(a)