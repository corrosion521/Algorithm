a,b,c = map(int,input().split())
day=1
while True:
    day+=1
    if day%a==0 and day%b==0 and day%c==0:
        break
print(day)