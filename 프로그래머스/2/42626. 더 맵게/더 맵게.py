import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville);
    
    cnt = 0
    while len(scoville) >= 2 and scoville[0] < K:
        cnt += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        result = first + (second * 2)
        heapq.heappush(scoville, result)

    
    return cnt if scoville[0] >= K else -1



