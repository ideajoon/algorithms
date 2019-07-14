def solution(m, n, puddles): # 첫번째 방법 : 성공
    L = [[False] * m for _ in range(n)] 
    
    for i in range(len(puddles)):
        y, x = puddles[i][0] - 1, puddles[i][1] - 1
        L[x][y] = 0
    
    for i in range(n):
        if L[i][0] is 0:
            break
        L[i][0] = 1
    
    for i in range(m):
        if L[0][i] is 0:
            break
        L[0][i] = 1
    
    for i in range(1, n):
        for j in range(1, m):
            if L[i][j] is False:
                L[i][j] = (L[i - 1][j] + L[i][j - 1]) % 1000000007

    return L[n - 1][m - 1] 

=========================================================================

def solution(m, n, puddles): # 두번째 방법 : 성공
    arr = [[0] * m for _ in range(n)] 
    arr[0][0] = 1
    
    for i in range(len(puddles)):
        y, x = puddles[i][0] - 1, puddles[i][1] - 1
        arr[x][y] = -1
    
    for j in range(1, n):
        if arr[j][0] == 0:
            arr[j][0] = arr[j - 1][0]
    
    for k in range(1, m):
        if arr[0][k] == 0:
            arr[0][k] = arr[0][k - 1]
    
    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j] == 0:
                if arr[i - 1][j] == -1 and arr[i][j - 1] == -1:
                    arr[i][j] = 0
                elif arr[i - 1][j] == -1:
                    arr[i][j] = arr[i][j - 1] % 1000000007
                elif arr[i][j - 1] == -1:
                    arr[i][j] = arr[i - 1][j] % 1000000007
                else:
                    arr[i][j] = (arr[i - 1][j] + arr[i][j - 1]) % 1000000007
    
    return arr[n - 1][m - 1]
