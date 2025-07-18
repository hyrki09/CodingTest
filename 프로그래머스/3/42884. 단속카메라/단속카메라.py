def solution(routes):
    count = 0
    camera_position = -300001
    routes.sort(key=lambda x:x[1])
    
    for route in routes:
        s,e = route
        
        if camera_position < s:
            camera_position = e
            count+=1
    return count