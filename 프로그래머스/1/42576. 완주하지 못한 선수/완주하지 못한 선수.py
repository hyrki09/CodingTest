from collections import Counter
def solution(participant, completion):
    
    p_count = Counter(participant)
    c_count = Counter(completion)
    
    last = p_count - c_count
    
    return list(last.keys())[0]