def solution(a, b, g, s, w, t):
    
    left = 0
    right = (10 ** 5) * (10 ** 9)* 4
    answer = right
    
    truck = len(g)
    
    # 이분 탐색
    while left <= right:
        
        total_gold = 0
        total_silver = 0
        total_both = 0
        
        time = (left + right) // 2
        
        for i in range(truck):
            round_trip_time = t[i] * 2
            trip = time // round_trip_time  # 도시로 전달하는 움직임 횟수
            
            if time % round_trip_time >= t[i]: # 편도
                trip += 1
                
            max_trip_weight = w[i] * trip # 현재 트럭이 갈수있는 최대 무게
            
            
            total_gold += min(g[i],max_trip_weight)  # 골드가 최대 일때
            total_silver += min(s[i],max_trip_weight) # 실버가 최대일때
            total_both += min(g[i] + s[i],max_trip_weight) # 합 무게
            
        if total_gold >= a and total_silver >= b and total_both >= a+b:
            # answer = min(answer,time)
            answer = time
            right = time - 1
        else:
            left = time + 1
            
    
    return answer