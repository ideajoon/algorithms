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
