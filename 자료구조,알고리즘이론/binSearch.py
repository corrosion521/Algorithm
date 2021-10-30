def binSearch(n,S,x,location):
    low = 0
    high = n-1
    location = 0

    while(low<=high and location==0):
        mid = (high+low)//2
        if S[mid] == x:
            location = mid
            break
        elif S[mid]>x:
            high = mid-1
        else:
            low = mid + 1
    return location

S = [1,2,3,4,5] #리스트
n = len(S) #리스트 길이
x = 4#찾고자 하는 값
location =0#찾고자 하는 값이 있을 경우의 위치, 없으면 0
location=binSearch(n,S,x,location)
print(location)#출력