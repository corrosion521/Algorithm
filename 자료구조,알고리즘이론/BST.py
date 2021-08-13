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
    return node
# 삭제하기 (remove,delete)
def remove(root,val):
    # 삭제하기 위해 삭제할 위치를 찾아줘야함.

    # 삭제할 값이 root의 값보다 작을 경우
    if val <root.val:
        #왼쪽으로 이동
        root.left = remove(root.left,val)
    elif val > root.val:
        # 오른쪽으로 이동
        root.right = remove(root.right,val)
    # 삭제할 애를 찾아서 작업을 시작해줍니다
    else:#val==root.val
        # 케이스를 여러가지로 나눠줘야 합니다
        # 1,2 자식이 하나이거나 둘일 경우, 자식 없는 경우도 처리가 가능하다 (어차피 None이기에)
        if root.left is None: # 왼쪽이 없다 == 오른쪽이 있거나 없다
            temp_node = root.right
            return temp_node
        elif root.right is None:
            temp_node = root.left
            return temp_node

        #자식 노드가 2개일 경우도
        #노드 오른쪽편에서 가장 왼쪽 것(가장 작은 값)을 찾습니다.
        temp_node = minimum(root.right)
        # node의 값을 오른쪽편에서 가장 작을 애를 넣어주고
        root.val = temp_node.val

        # temp_node.val에 값을 삭제해줍니다.
        # root의 오른쪽편에서 가장 왼쪽에 있는 값을 삭제해주면
        # root에 temp_node.val의 값이 들어가고
        # temp_node를 삭제해주면 BST형태가 갖춰집니다.
        root.right = remove(root.right,temp_node.val)

    return root


root = None
root = insert(root,50)
root = insert(root,30)
root = insert(root,20)
root = insert(root,40)
root = insert(root,70)
root = insert(root,60)
root = insert(root,80)

root = remove(root,50)

inorder(root)#20 30 40 60 70 80
print("root",root.val)