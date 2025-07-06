def solution(n, lost, reserve):
    answer = 0
    
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    # print(set_lost)
    # print(set_reserve)
    
    
    for i in sorted(set_reserve):
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
            
    
    # print(set_lost)
            
    return n - len(set_lost)