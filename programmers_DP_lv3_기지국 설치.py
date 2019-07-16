import math

def solution(n, stations, w):
    stations.sort()
    diff = []
    
    if stations[0] != 1:
        diff.append(stations[0] - 1 - w)
            
    for i in range(len(stations) - 1):
        diff.append(stations[i + 1] - stations[i] - 1 - (2 * w))
        
    if stations[-1] != n:
        diff.append(n - stations[-1] - w)
        
    notcover_area = [x for x in diff if x > 0]
    ans_list = [math.ceil(x / (2 * w + 1)) for x in notcover_area]
    
    ans = sum(ans_list) 
    
    return ans



# def solution(n, stations, w):
#     stations.sort()
#     spread_area = []
#     for i in range(len(stations)):
#         if stations[i] - w <= 0:
#             spread_area.append([1, stations[i] + w])
#         elif stations[i] + w > n:
#             spread_area.append([stations[i] - w, n])
#         else:    
#             spread_area.append([stations[i] - w, stations[i] + w])
#     print(spread_area)
        
def solution(n, stations, w):
    answer = 0
    cover = 0
    width = 2 * w + 1
    for station in stations:
        if station - w > cover + 1:
            answer += (station - w - 1 - cover) // width
            if (station - w - 1 - cover) % width > 0:
                answer += 1
        cover = station + w
    if cover < n:
        answer += (n - cover) // width
        if (n - cover) % width > 0:
            answer += 1
    return answer  


#n = 11
#stations = [4, 11]
#w = 1
#answer = 3

#참고 : https://school.programmers.co.kr/courses/10021/lessons/58509
#참고 : https://velog.io/@songjy6565/%EA%B8%B0%EC%A7%80%EA%B5%AD-%EC%84%A4%EC%B9%98
