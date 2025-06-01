from collections import deque
def solution(priorities, location):
    
    queue = deque([(i,p) for i,p in enumerate(priorities)])
    
    seq = 0
    while queue:
        cur_p = queue.popleft()
        if any(cur_p[1] < q[1] for q in queue):
            queue.append(cur_p)
        else:
            seq += 1
            if cur_p[0] == location:
                return seq;
            