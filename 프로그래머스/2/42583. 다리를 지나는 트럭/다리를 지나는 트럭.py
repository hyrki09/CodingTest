from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    w_queue = deque([bridge_length,weight] for weight in truck_weights)
    
    bridge_queue = deque()
    bridge_queue.append(w_queue.popleft())
    time = 1
    
    while bridge_queue:
        n =len(bridge_queue)
        for i in range(n):
            bridge_queue[i][0] -= 1
            
        move, w = bridge_queue[0]
        time +=1
        
        if move == 0:
            bridge_queue.popleft()
    
        sum_weight = sum(map(lambda x: x[1], bridge_queue))
        
        if w_queue and sum_weight + w_queue[0][1] <= weight :
            bridge_queue.append(w_queue.popleft())
            
    return time