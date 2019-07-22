def solution(x):
    if x == 0:
        answer = 0
    elif x == 1:
        answer = 1
    else:
        answer = solution(x-1) + solution(x-2)
    return answer
