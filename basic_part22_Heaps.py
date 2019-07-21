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
