import math
from collections import deque
def solution(progresses, speeds):
    n = len(progresses)
    time_list = deque()
    answer = []
    for i in range(n):
        time_list.append(math.ceil((100 - progresses[i])/speeds[i]))
    
    front_work_time = time_list.popleft()
    count = 1
    
    while time_list:
        f_time = time_list.popleft()
        
        if front_work_time >= f_time:
            count += 1
        else:
            print(time_list)
            answer.append(count)
            front_work_time = f_time
            count = 1
    answer.append(count)
    
    return answer