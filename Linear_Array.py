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
    
    
