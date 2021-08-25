'''
원-원 접점의 개수?
반지름과 원의 각점의 거리를 이용하면 됨
(이미 아는 내용)
'''


# 입력 : testcase, 규현 승환 좌표, 반지름
t = int(input())
for i in range(t):
    a,b,r,c,d,k=map(int,input().split())
    dis=((c-a)**2+(d-b)**2)**(1/2)# 두 사람 좌표의 거리
    if a==c and b==d:#위치가 같을 때
        if r==k:#반지름이 같으면
            print("-1")#접점 무한
        else:
            print("0")#접점 x
    else:#위치가 다를 때
        if  r+k>dis and abs(r-k)<dis:#원끼리 접하는 지점이 있는 경우
            print("2")#접점 두개
        elif r+k==dis or abs(r-k)==dis:#외,내접
            print("1")
        elif r+k<dis or abs(r-k)>dis:# 바깥쪽에 있어서 안만나거나, 안쪽에서 안만나거나(좌표는 다름)
            print("0")#접점 x



'''
중심으로 부터의 동일거리 - 원 형성 !
마찬가지로 좌표이용한 수학 문제는 그림을 직접 그려보면 답나옴
그냥 수학코딩문제도 수학문제랑 같다. 구현 방법에 있어 차이가 나는거지.
역시 문제인 만큼 세부조건 주의해야함. 덜렁거리지 마라
'''