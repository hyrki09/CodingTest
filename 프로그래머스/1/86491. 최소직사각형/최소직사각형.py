

def solution(sizes):
    answer = 0
    
    x_list = []
    y_list = []
    
    for [i,j] in sizes:
        
        x_list.append(max(i,j))
        y_list.append(min(i,j))
    
    
    
    return max(x_list) * max(y_list)