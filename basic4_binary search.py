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
