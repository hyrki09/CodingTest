def solution(arr):
    answer = []
    
    x = ''
    
    for num in arr:
        if x != num:
            answer.append(num)
        x = num
            
        
    return answer