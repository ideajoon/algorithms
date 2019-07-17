# 정렬된 리스트에 원소 삽입
# 리스트 L 과 정수 x 가 인자로 주어질 때, 리스트 내의 올바른 위치에 x 를 삽입하여 
# 그 결과 리스트를 반환하는 함수 solution 을 완성하세요.

def solution(L, x):
    for i in range(len(L)):
        if L[i] >= x:
            L.insert(i, x)
            break
        elif L[-1] < x:
            L.append(x)
            break        
    answer = L
    return answer

# 참고 : https://programmers.co.kr/learn/courses/57/lessons/13773


# 리스트에서 원소 찾아내기
# 인자로 주어지는 리스트 L 내에서, 또한 인자로 주어지는 원소 x 가 발견되는 모든 인덱스를 구하여 
# 이 인덱스들로 이루어진 리스트를 반환하는 함수 solution 을 완성하세요.

def solution(L, x):
    if x in L:
        a = [i for i, n in enumerate(L) if n == x ]
    else:
        a = [-1]
    answer = a
    return answer

# 참고 : https://programmers.co.kr/learn/courses/57/lessons/13774
