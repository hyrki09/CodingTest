def solution(n):
    
    cnt = 0
    for i in range(4,n+1):
        for j in range(2,i):
            if i % j == 0:
                cnt +=1
                break
            
    return cnt