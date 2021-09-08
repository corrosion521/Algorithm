#함수: 이진 탐색 (재귀)
def BSR(arr,first,last,target):
    mid = (first+last)//2

    if first>last:
        return -1
    if target == arr[mid]:
        return mid
    elif target>arr[mid]:
        return BSR(arr,mid+1,last,target)
    else:
        return BSR(arr,first,mid-1,target)

#입력 : 배열
print("배열을 입력하라:",end='')
arr = list(map(int,input().split()))

#입력 : 타겟
print("target은?:",end='')
target = int(input())

k=len(arr)-1

#계산:함수이용
result = BSR(arr,0,k,target)

#출력
if result>=0:
    print("target은" ,result+1,"번째")
else:
    print("target 찾기 실패")

'''
python 에서는 / 이게 몫이 아니라 진짜 생나누기임 //로 해야 된다.
TypeError: list indices must be integers or slices, not float

'''