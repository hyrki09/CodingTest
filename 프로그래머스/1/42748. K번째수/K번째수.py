def solution(array, commands):
    answer = []
    
    for i,j,k in commands:
        com_list = array[i-1:j]
        com_list.sort()
        
        answer.append(com_list[k-1])

    return answer