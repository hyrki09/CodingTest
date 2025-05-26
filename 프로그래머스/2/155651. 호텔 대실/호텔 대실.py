import heapq
def solution(book_time):
    answer = 0
    room_list = []
    
    time_list = []
    for s,e in book_time:
        s_hour, s_min = map(int, s.split(':'))
        start_time = s_hour * 60 + s_min
        e_hour, e_min = map(int, e.split(':'))
        end_time = e_hour * 60 + e_min + 10
        
        time_list.append((start_time, end_time))
        time_list.sort()
        
        
    print(time_list)
    
    
    room = []
    
    for start,end in time_list:
        
        # print(room)
        if room and room[0] <= start:
            heapq.heappop(room)
        
        heapq.heappush(room, end)
        
        
            
        
    return len(room)