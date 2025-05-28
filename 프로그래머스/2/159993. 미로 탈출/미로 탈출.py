from collections import deque

def bfs(start, target_char, maps):
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append((start[0], start[1], 0)) 
    visited[start[0]][start[1]] = True

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while q:
        x, y, dist = q.popleft()
        if maps[x][y] == target_char:
            return (x, y, dist)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))
    
    return None  

def solution(maps):
    n, m = len(maps), len(maps[0])
    S = None

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                S = (i, j)
                break
        if S:
            break

    to_lever = bfs(S, 'L', maps)
    if to_lever is None:
        return -1 

    to_exit = bfs((to_lever[0], to_lever[1]), 'E', maps)
    if to_exit is None:
        return -1 

    return to_lever[2] + to_exit[2]
