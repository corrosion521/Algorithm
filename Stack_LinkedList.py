# Node를 만들어줍니다.
class Node :

    def __init__(self,data):
        self.data = data
        self.next = None

# Stack을 만들어줍니다.
class Stack :

    # Head를 만들고
    def __init__(self):
        self.head = None # head 생성

    # Stack 쌓아줍니다.
    def push(self,data):

        # Stack이 비어있을 때,아무것도 가리키지 않을 때
        if self.head is None:
            self.head = Node(data)#헤드가 push된 Node를 가리키게 함

        # Stack이 비어있지 않을 때
        else:
            new_node = Node(data)#새 노드 완성 / 새 노드 생성 후 레퍼런스를 새 노드에 저장
            new_node.next = self.head #새 노드의 next가 전 노드를 가리키게함/ stack의 head에 있는 전 Node의 레퍼런스를 new_node의 next에 넣어, new_node가 전 Node를 가리키게 함.
            self.head = new_node #head가 new_node를 가리킴

    # Stack 빼주는 것들
    def pop(self):

        # Stack이 비었을 때
        if self.head is None:
                return None

        # Stack이 비어있지 않을 때
        else:
            popped = self.head.data #data를 popped에 담음
            self.head = self.head.next #head가 빼주려는 노드가 가리키는 노드(그 아래의 노드)를 가리키게함
            return popped #그 노드의 data를 반환

s = Stack()

s.push("a")
s.push("b")
s.push("c")
s.push("d")
s.push("e")

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

print(s.pop())