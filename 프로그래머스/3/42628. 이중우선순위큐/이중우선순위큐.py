import heapq

def solution(operations):
    
    h = []
    
    
    for command in operations:
        
        command_line = command.split()
        cm_str = command_line[0]
        cm_num = command_line[1]
        
        if cm_str == "I":
            heapq.heappush(h, int(cm_num))
        else:
            if cm_num == "1":
                h=heapq.nlargest(len(h), h)[1:]
                heapq.heapify(h)
            elif cm_num == "-1" and len(h) > 0:
                heapq.heappop(h)

    return [max(h), h[0]] if h else [0,0]