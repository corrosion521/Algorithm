'''
1.이진탐색(binary search):
1)찾고자 하는 값과 자료 가운데 항목의 값과 비교하며 검색 범위를 줄여나감
2)큰 자료를 검색할 경우 유용
3)로직 - 아래 과정 반복
1. 자료 중앙원소 고름
2. 중앙원소 VS 목표값
2. 중앙원소 VS 목표값
1> 목표값 < 중앙원소 => 왼쪽 반에 대해 검색
2> 목표값 > 중앙원소 => 오른쪽 반에 대해 검색
4) 다만, 정렬된 리스트에서만 사용 가능하다.

'''
# 이진탐색 
def binsearch(target,n_list,n):
    left =0
    right = n-1

    while left<=right: # 등호 있는 이유: 당연하지만 등호가 성립할 때 left==right==target 일때 타겟이 탐색완료되기 때문이다.
        mid = (left + right) // 2 # 매번 mid가 갱신된다.
        if target == n_list[mid]: # 같을 경우 (탐색완료)
            return True
        elif target < n_list[mid]: # 타겟이 오른쪽 일경우
            right = mid-1 
        elif target > n_list[mid]: # 왼쪽
            left = mid+1

n = int(input()) # 비교판 개수
n_list = list(map(int,input().split())) # 비교판 입력
n_list.sort()# 이진 탐색해야 하므로(비교판) , 정렬 해둠.

m = int(input()) # 데이터 개수
m_list = list(map(int,input().split())) # 데이터 입력

# 데이터 하나 씩 비교판이랑 비교
for i in range(m):
    if binsearch(m_list[i],n_list,n):# 이진탐색(데이터하나, 비교판,비교판 개수)
        print("1") # 있으면 1
    else:
        print("0") # 없으면 0 
