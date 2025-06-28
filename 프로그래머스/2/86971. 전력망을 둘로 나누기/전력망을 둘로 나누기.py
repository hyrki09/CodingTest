
from collections import deque
def solution(n, wires):
    answer = float('inf')
    # answer =-1
    
    for i in range(len(wires)):
        temp_wires = wires[:i] + wires[i+1:]

        graph = [[] for _ in range(n+1)]
        for a,b in temp_wires:
            graph[a].append(b)
            graph[b].append(a)
            
        visited_list = [False] * (n+1)
        visited_list[1] = True
        q=deque([1])
        cnt = 1
            
        while q:
            e_top=q.popleft()
            for link_top in graph[e_top]:
                if not visited_list[link_top]:
                    visited_list[link_top] = True
                    q.append(link_top)
                    cnt +=1
        diff = abs(n-cnt-cnt)
        answer = min(answer,diff)
            
    return answer