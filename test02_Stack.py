def solution(list):
    sort_list = sorted(list)
    reverse_list = sorted(list, reverse = True)
    stack = []
    ans = []
    idx = 0
    compare = list[idx]
    for num in sort_list:
        if not stack:
            temp = reverse_list.pop()
            stack.append(temp)
        else:
            if stack[-1] == compare:
                while stack:
                    temp = stack.pop()
                    ans.append(temp)                
                stack.append(num)
                idx += 1
                compare = list[idx]
            else:
                stack.append(num)
    
    while stack:
        temp = stack.pop()
        ans.append(temp)
  
    if ans == list:
        return True
    else:
        return False
