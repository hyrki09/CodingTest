from collections import deque
def solution(maps):
    answer = []
    # map_list = [list(i) for i in maps]
    n,m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    result = []
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                q =deque()
                q.append((i,j))
                days = int(maps[i][j])
                visited[i][j] = True
                while q:
                    x,y = q.popleft()
                    for dx, dy in directions:
                        nx, ny = x+dx, y+dy
                        if 0<=nx<n and 0<=ny<m and maps[nx][ny] != 'X' and not visited[nx][ny]:
                            q.append((nx, ny))
                            days += int(maps[nx][ny])
                            visited[nx][ny] = True
                result.append(days)
    
    return sorted(result) if result else [-1]