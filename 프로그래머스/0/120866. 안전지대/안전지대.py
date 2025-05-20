def solution(board):
    answer = 0
    size = len(board)
    safe_zone = [[0] * size for _ in range(size)]
    
    danger_zone = [
        [-1,-1],[0,-1],[1,-1],
        [-1,0],[0,0],[1,0],
        [-1,1],[0,1],[1,1]
    ]
    
    
    for i in range(size):
        for j in range(size):
            if board[i][j] == 1:
                for dx, dy in danger_zone:
                    sx = i+dx
                    sy = j+dy
                    if 0<=sx<size and 0<=sy<size:
                        safe_zone[sx][sy]=1
        
    for hang in safe_zone:
        for val in hang:
            if val == 0:
                answer +=1
    
    
    return answer