def solution(s):
    answer = ''
    str_list = list(s)
    str_list.sort()
    str_list.reverse()
    
    return ''.join(str_list)