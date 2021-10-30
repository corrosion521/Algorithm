def seqSearch(n,S,x,location):
    while(S[location]!=x and location<=n):
        location+=1

    if (location>n):
        location = 0
    return location

S = [5,4,3,2,1] #리스트
n = len(S) #리스트 길이
x = 3#찾고자 하는 값
location =0#찾고자 하는 값이 있을 경우의 위치, 없으면 0
location=seqSearch(n,S,x,location)
print(location)#출력