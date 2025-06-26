from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    root_list = []
    for roots in permutations(dungeons,len(dungeons)):
        remain_k = k
        cnt = 0
        for min_fatigue, use_fatigue in roots:
            if remain_k >= min_fatigue:
                cnt+=1
                remain_k -= use_fatigue
            else:
                break
        root_list.append(cnt)
        
                
        
    return max(root_list)