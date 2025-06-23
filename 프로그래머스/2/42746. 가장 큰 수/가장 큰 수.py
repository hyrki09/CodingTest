
def solution(numbers):
    
    num_str_list = list(map(str, numbers))    
    num_str_list.sort(key=lambda x:x*3, reverse=True)
    
    result = ''.join(num_str_list)
    
    return "0" if result[0] == '0'else result