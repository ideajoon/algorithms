def solution(s): # DP 문제
    n = len(s)
    L = [[0] * n for _ in range(n)]
    longest_palindrome = 0
      
    for i in range(n):
        for j in range(n - i):
            # n < 3 일 경우, substring의 끝이 같을 경우 
            # True를 넣고, longest_palindrome 을 업데이트 한다
            if i < 2:
                if s[j] == s[i + j]:
                    L[j][i + j] = True
                    longest_palindrome = i + 1
                else:
                    L[j][i + j] = False
            # n > 3 일 경우
            # substring의 끝이 같고, 왼쪽 밑 대각선 한칸에 있는 박스가 True면 
            # True를 넣고, longest_palindrome을 업데이트 한다.
            else:
                if s[j] == s[i + j] and L[j + 1][i + j - 1]:
                    L[j][i + j] = True
                    longest_palindrome = i + 1                    
                else:
                    L[j][i + j] = False
    return longest_palindrome
