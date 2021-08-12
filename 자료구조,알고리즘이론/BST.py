'''
출처: 인프런 강의

지구에서 제일 쉽게 설명한 자료구조와 알고리즘- 개복치 개발자

수업 때 들은 내용을 바탕으로 간략하게 요약한 내용입니다. 틀린 내용이 있거나 고쳐야 할 점이 있다면 가르쳐주신다면 감사하겠습니다.

문제가 될 시 바로 게시글 내리도록 하겠습니다.

﻿https://www.inflearn.com/course/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-1/dashboard

'''
# 노드 생성
class Node :
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

# 추가하기
def insert(node,val) :

    # 만약에 root가 비어 있을 때
    # node를 root로 만들어 준다.
    if node is None:
        return Node(val)

    #만약 root의 val값이 val값보다 클 경우
    if val < node.val:
        # 왼쪽으로 이동
        node.left = insert(node.left,val)
    # 만약 root의 val값이 val 봐다 작을 경우
    else :
        #오른쪽으로 이동
        node.right = insert(node.right,val)

    #root의 값을 리턴
    return node
# inorder
def inorder(root) :
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
# 가장 작은 값 출력
def minimum(node):

    # 노드가 가장 왼쪽으로로 가면 되겠죠?
    while (node.left is not None):
        node = node.left

    # 가장 왼쪽에 있는 애를 리턴
    return node.val

root = None
root = insert(root,50)
root = insert(root,30)
root = insert(root,20)
root = insert(root,40)
root = insert(root,70)
root = insert(root,60)
root = insert(root,80)

inorder(root)#20 30 40 50 60 70 80
print(minimum(root))