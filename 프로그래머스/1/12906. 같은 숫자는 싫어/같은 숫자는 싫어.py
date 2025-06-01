def solution(arr):
    answer = []
    answer.append(arr[0])
    x = arr[0]
    
    for num in arr:
        if x != num:
            answer.append(num)
            x = num
            
        
    return answer