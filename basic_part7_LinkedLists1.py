(07) 연결 리스트 순회
제 7 강에서 소개된 추상적 자료구조로 LinkedList 라는 이름의 클래스가 정의되어 있다고 가정하고, 
이 리스트를 처음부터 끝까지 순회하는 메서드 traverse() 를 완성하세요.
메서드 traverse() 는 리스트를 리턴하되, 이 리스트에는 연결 리스트의 노드들에 들어 있는 데이터 
아이템들을 연결 리스트에서의 순서와 같도록 포함합니다. 예를 들어, LinkedList L 에 들어 있는 노드들이 
43 -> 85 -> 62 라면, 올바른 리턴 값은 [43, 85, 62] 입니다.
이 규칙을 적용하면, 빈 연결 리스트에 대한 순회 결과로 traverse() 메서드가 리턴해야 할 올바른 결과는 [] 입니다.
[참고] 실행 을 눌렀을 때 통과하는 것은 아무 의미 없습니다.


class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0 #노드의 개수
        self.head = None #1번째 노드는 아무것도 가르키고 있지 않다.
        self.tail = None #마지막 노드는 아무것도 가르키고 있지 않다.

    def getAt(self, pos): #pos:노드 인덱스 번호, 즉 pos번째의 노드를 불러와라
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        curr = self.head
        answer = []
        while curr is not None:
            answer.append(curr.data)
            curr = curr.next
        return answer


# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0
