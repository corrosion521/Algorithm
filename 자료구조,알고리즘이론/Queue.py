
'''
출처: 인프런 강의

지구에서 제일 쉽게 설명한 자료구조와 알고리즘- 개복치 개발자

수업 때 들은 내용을 바탕으로 간략하게 요약한 내용입니다. 틀린 내용이 있거나 고쳐야 할 점이 있다면 가르쳐주신다면 감사하겠습니다.

문제가 될 시 바로 게시글 내리도록 하겠습니다.

﻿https://www.inflearn.com/course/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-1/dashboard


'''

# Node 생성

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None#파이썬에서는 Null이 아니라 None

# Queue 만들기

class Queue :
    # head,tail 생성
    def __init__(self):
        self.head = None
        self.tail = None

    #비어 있는지 확인하는 isEmpty,head를 체크
    def isEmpty(self):
         if self.head is None :
            return True
         else :
             return False

    # enqueue Add
    def enqueue(self,data):
       #Queue가 비어있을 때,tail 체크
       if self.tail is None:
            self.head = self.tail =Node(data)#head,tail 모두 노드를 가리킴(비어 있는 상태에서 노드가 하나 뿐이기에 그 노드가 테일,헤드 모두 지칭당함)

       #Queue가 비어있지 않을 때
       else:
            #새로운 node를 생성해서 뒤에 붙이고
            self.tail.next = Node(data)# tail이 가리키는 노드의 next가 새로운 노드를 가리킴
            #tail의 위치를 조정해줍니다.
            self.tail = self.tail.next

    #dequeue Remove
    def dequeue(self):

        # Queue가 비어있을 때
        if self.head is None :
            return None

        # Queue가 비어있지 않을 때
        else:
            dequeue_data = self.head.data
            self.head = self.head.next
            return dequeue_data


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())#1
print(q.dequeue())#2
print(q.dequeue())#3
print(q.isEmpty())#False
print(q.dequeue())#4
print(q.isEmpty())#True


