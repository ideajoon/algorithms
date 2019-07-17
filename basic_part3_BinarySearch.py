# 리스트 L 과, 그 안에서 찾으려 하는 원소 x 가 인자로 주어질 때, x 와 
# 같은 값을 가지는 원소의 인덱스를 리턴하는 함수 solution() 을 완성하세요. 
# 만약 리스트 L 안에 x 와 같은 값을 가지는 원소가 존재하지 않는 경우에는 -1 을 리턴합니다. 

def solution(L, x):
    lower = 0
    upper = len(L) - 1
    idx = -1
    if x in L:
        while lower <= upper:
            middle = (lower + upper) // 2
            if L[middle] == x:
                answer = middle
                break
            elif L[middle] < x:
                lower = middle + 1
            else:
                upper = middle - 1
    else:
        answer = idx

    return answer
    
    # 참고 : https://programmers.co.kr/learn/courses/57/lessons/13775
