

def solution(brown, yellow):
    answer = []
    
    num_list = []
    min_number = yellow;
    for i in range(1,yellow+1):
        if i >= min_number:
            break
        if yellow % i == 0:
            min_number = (int)(yellow / i)
            num_list.append((min_number,i))
    num_list = [(1,1)] if not num_list else num_list
    
    print(num_list)
    for x,y in num_list:
        round_len = (x+y)*2 + 4
        if round_len == brown:
            return [x+2, y+2]
        
    
    
    return answer