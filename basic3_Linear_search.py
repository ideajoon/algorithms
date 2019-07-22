def linear_search(L, x):
    i = 0
    while i < len(L) and L[i] i= x:
        i += 1
    if i < len(L):
        return i
    else:
        return -1
