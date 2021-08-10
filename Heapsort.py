'''
출처: 인프런 강의

지구에서 제일 쉽게 설명한 자료구조와 알고리즘- 개복치 개발자

수업 때 들은 내용을 바탕으로 간략하게 요약한 내용입니다. 틀린 내용이 있거나 고쳐야 할 점이 있다면 가르쳐주신다면 감사하겠습니다.

문제가 될 시 바로 게시글 내리도록 하겠습니다.

https://www.inflearn.com/course/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-1/dashboard


'''
#heapify 동작
def heapify(list,n,i):

    root_largest = i
    left = 2 * i + 1
    right = 2 * i +2

    #왼쪽 애가 존재하고
    #왼쪽 애가 루트보다 더 클 때
    if left < n and list[i] < list[left] :
        root_largest = left

    # 오른쪽 애가 존재하고
    # 오른쪽 애가 루트보다 더 클 때
    if right < n and list[root_largest]<list[right]:
        root_largest = right

    # 왼쪽, 오른쪽 자식들과 바꿔줘야 할 위치를 찾았을 때
    if root_largest !=i:
        # 찾아낸 값이랑 Swap
        list[i], list[root_largest] = list[root_largest],list[i]
        #계속 heap의 형태를 갖출 때까지 실행, (!) 위치를 바꾸면 그 아래의 노드들과의 대소관계도 바뀔 수 있다는 것이기에 다시 heapify해줘야한다.
        heapify(list,n,root_largest)


#heapsort
def heapSort(list):
    n = len(list)

    #heap의 형태로 데이터를 저장하기
    for i in range(n,-1,-1): #C B T  중 가장 아래(마지막)의 노드부터 접근한다.
       heapify(list,n,i)

    # root에 있는 애랑, 마지막에 있는 애를 바꿔서 정렬해주고
    # 바뀐 애를 기준으로 다시 heapify를 실행합니다.
    for i in range(n-1,0,-1):
        list[i],list[0] = list[0],list[i] # (!) 노드가 바뀌니(루트도트<->마지막노드) 다시 그 바뀐 노드(현 루트노드) 기준으로 heapify해줘야한다.
        heapify(list,i,0) #i에 주목. i는 n이 아니라 n-1인데 이는 마지막 노드(이미 정렬된 노드, 여기서는 처음엔 10)를 제외하고 heapify를 한다는 뜻이다.
                          #heapify 한 번이 끝나면 루트노드가 가장 크게 된다. 다음 반복문이 돌면 그 루트노드가 마지막 노드로 이동하고 정렬된다.

list = [4, 10, 3, 5, 1]
print("Start : ",list)
heapSort(list)
print("result : ", list)