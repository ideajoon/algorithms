(22) 최대 힙에 새로운 원소 삽입
초기 코드에 주어진 class MaxHeap 에 최대 힙에 새로운 원소를 추가하는 연산인 insert() 메서드의 구현을 완성하세요.
[참고 1] solution() 함수의 구현은 그대로 두세요. 이것을 없애면 테스트가 되지 않습니다.
[참고 2] 코드 실행 을 눌렀을 때 통과하는 것은 아무런 의미가 없습니다.


class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        idx_item = len(self.data) - 1
        idx_parent = idx_item // 2
        
        while idx_item > 1: 
            if self.data[idx_item] > self.data[idx_parent]:
                self.data[idx_parent], self.data[idx_item] = self.data[idx_item], self.data[idx_parent]
                idx_item = idx_parent
                idx_parent = idx_item // 2
            else:
                break
            


def solution(x):
    return 0
