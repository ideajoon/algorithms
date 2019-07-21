(10-2) 양방향 연결 리스트 노드 삽입
제 10 강에서 소개된 추상적 자료구조 DoublyLinkedList 의 메서드로 insertBefore() 를 구현하세요.
이 insertBefore() 메서드에는 두 개의 인자가 주어지는데, next 는 어느 node 의 앞에 새로운 node 를 삽입할지를 지정하고,
newNode 는 삽입할 새로운 node 입니다.
강의 내용에서 소개된 insertAfter() 메서드의 구현과 매우 유사하게 할 수 있습니다.


class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def insertBefore(self, next, newNode):
        prev = next.prev
        newNode.next = next
        newNode.prev = prev
        next.prev = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True        


def solution(x):
    return 0
