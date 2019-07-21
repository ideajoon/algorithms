(21) 이진 탐색 트리에서 노드의 삭제 연산 구현
초기 코드에 주어진 class Node 와 class BinSearchTree 를 기반으로, 
이진 탐색 트리 (binary search tree) 에서 지정된 원소를 삭제하는 remove(key) 연산의 구현을 완성하세요.
class Node 와 class BinSearchTree 에 이미 구현되어 있는 코드는 수정하지 마세요. 
코드 구현의 정확성 평가에 이용됩니다. 초기 코드에 들어 있는 주석을 참고로 하여, 
BinSearchTree::remove() 메서드의 안에 들어 있는 pass 를 없애고 그 자리에 올바른 코드를 써 넣으면 됩니다.
[참고 1] solution() 함수의 구현은 그대로 두세요. 이것을 없애면 테스트가 되지 않습니다.
[참고 2] 코드 실행 을 눌렀을 때 통과하는 것은 아무런 의미가 없습니다.
[참고 3] 잘 생각해 보면, 이진 탐색 트리를 구현하지 않고 키 순서대로 
정렬된 Python 의 배열을 유지함으로써도 같은 연산을 구현할 수 있습니다. 
이 연습문제에서는 효율성 테스트를 하지 않기 때문에 이러한 구현을 오답으로 간주하지 않습니다만, 
배열을 이용한 구현과 트리 구조를 이용한 구현은 연산의 복잡도에 큰 차이가 있습니다. 
이진 탐색 트리로 구현하여 코드 작성 연습을 하시기 바랍니다.


class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError('Key %s already exists.' % key)


    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count


class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None


    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # The simplest case of no children
            if nChildren == 0:
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여
                # leaf node 였던 자식을 트리에서 끊어내어 없앱니다.
                if parent:
                    if node.key < parent.key:
                        parent.left = None
                    else:
                        parent.right = None
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 를 None 으로 하여 빈 트리로 만듭니다.
                else:
                    self.root = None
            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.
                if node.left:
                    nodechild = node.left
                else:
                    nodechild = node.right 
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
                if parent:
                    if node.key < parent.key:
                        parent.left = nodechild
                    else:
                        parent.right = nodechild
                        
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 에 위에서 가리킨 자식을 대신 넣습니다.
                else:
                    self.root = nodechild
            # When the node has both left and right children
            else:
                parent = node
                successor = node.right
                # parent 는 node 를 가리키고 있고,
                # successor 는 node 의 오른쪽 자식을 가리키고 있으므로
                # successor 로부터 왼쪽 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor 는 바로 다음 키를 가진 노드를,
                # 그리고 parent 는 그 노드의 부모 노드를 가리키도록 찾아냅니다.
                while successor.left:
                    parent = successor
                    successor = successor.left
                # 삭제하려는 노드인 node 에 successor 의 key 와 data 를 대입합니다.
                node.key = successor.key
                node.data = successor.data
                # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                # 그에 따라 parent.left 또는 parent.right 를
                # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.
                if successor.key < parent.key:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

            return True

        else:
            return False


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


def solution(x):
    return 0
