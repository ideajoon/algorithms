(23) 최대 힙에서의 원소 삭제
초기 코드에 여기 저기 포함된 빈 칸을 채움으로써 class MaxHeap 의 메서드인 maxHeapify() 의 구현을 완성하세요. 
이것은 이미 주어져 있는 remove() 메서드와 연결되어 최대 힙에서의 원소 삭제 연산을 구성합니다.
[참고 1] remove() 메서드의 내용은 이미 주어져 있으므로 수정하지 않는 쪽이 좋습니다.
[참고 2] solution() 함수의 구현은 그대로 두세요. 이것을 없애면 테스트가 되지 않습니다.
[참고 3] 코드 실행 을 눌렀을 때 통과하는 것은 아무런 의미가 없습니다.



class MaxHeap:

    def __init__(self):
        self.data = [None]


    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data


    def maxHeapify(self, i):
        # 왼쪽 자식 (left child) 의 인덱스를 계산합니다.
        left = 2 * i
        # 오른쪽 자식 (right child) 의 인덱스를 계산합니다.
        right = 2 * i + 1
        greatest = i
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if left <= len(self.data) - 1 and self.data[left] > self.data[greatest]:
            # 조건이 만족하는 경우, greatest 는 왼쪽 자식의 인덱스를 가집니다.
            greatest = left
        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if right <= len(self.data) - 1 and self.data[right] > self.data[greatest]:
            # 조건이 만족하는 경우, greatest 는 오른쪽 자식의 인덱스를 가집니다.
            greatest = right
        if greatest != i:
            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[i], self.data[greatest] = self.data[greatest], self.data[i]
            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(greatest)


def solution(x):
    return 0
