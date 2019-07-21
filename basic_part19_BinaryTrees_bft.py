(19) 이진 트리의 넓이 우선 순회
이진 트리를 구현한 클래스인 class BinaryTree 에 대하여 넓이 우선 순회 (breadth first traversal) 
를 구현하는 메서드 bft() 를 완성하세요.
class ArrayQueue 는 배열 (python list) 을 이용하여 구현한 큐 (queue) 의 추상적 자료구조입니다. 
이것을 이용하여 넓이 우선 순회 알고리즘을 구현하세요.
[참고 1] solution() 함수의 구현은 그대로 두세요. 이것을 없애면 테스트가 되지 않습니다.
[참고 2] 코드 실행 을 눌렀을 때 통과하는 것은 아무런 의미가 없습니다.


class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def bft(self):
        traversal = []
        q = ArrayQueue()
        if self.root:
            q.enqueue(self.root)
        while not q.isEmpty():
            node = q.dequeue()
            traversal.append(node.data)
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
        
        return traversal
            


def solution(x):
    return 0
