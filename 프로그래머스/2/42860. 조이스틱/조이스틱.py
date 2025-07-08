def solution(name):
    answer = 0
    
    for i in name:
        answer += min(ord(i) - ord('A'), ord('Z')-ord(i)+1)
    min_move = len(name) -1
    for i in range(len(name)):
        next_idx = i + 1
    
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        move = i + i + (len(name) - next_idx)
        move2 = (len(name) - next_idx) * 2 + i
        min_move = min(min_move, move, move2)

    answer += min_move
    
        
    
    return answer