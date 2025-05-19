import heapq
def solution(jobs):
    answer = 0
    jobs.sort()
    heap = []
    time = 0
    total_time = 0
    i=0
    count = len(jobs)
    
    
    while i < count or heap:
        
        while i < count and jobs[i][0] <= time:
            request, work = jobs[i]
            heapq.heappush(heap, (work, request))
            i += 1
            
        if heap:
            work, request = heapq.heappop(heap)
            time += work
            total_time += time - request
        else:
            time = jobs[i][0]
          
    return total_time // count