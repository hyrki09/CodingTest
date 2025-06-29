def solution(word):
    order = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    weights = [781, 156, 31, 6, 1]
    
    
    answer = 0
    for i, ch in enumerate(word):
        answer += order[ch] * weights[i]+1
    return answer
