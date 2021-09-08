#함수: 이진 탐색 (반복문)
def BSL(arr,first,last,target):
    while True:
        mid = (first + last) // 2
        if first>last:
            return -1
        if target == arr[mid]:
            return mid
        elif target>arr[mid]:
            first = mid + 1
        else:
            last = mid - 1

#입력 : 배열
print("배열을 입력하라:",end='')
arr = list(map(int,input().split()))

#입력 : 타겟
print("target은?:",end='')
target = int(input())

k=len(arr)-1

#계산:함수이용
result = BSL(arr,0,k,target)

#출력
if result>=0:
    print("target은" ,result+1,"번째")
else:
    print("target 찾기 실패")

'''
python 에서는 / 이게 몫이 아니라 진짜 생나누기임 //로 해야 된다.
TypeError: list indices must be integers or slices, not float

디버그하다, print디버그 고루 사용하기. 

'''