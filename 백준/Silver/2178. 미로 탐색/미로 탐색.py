import sys
from collections import deque

input_data= sys.stdin.readline


conditional_str=list(map(int, input_data().strip().split()))

n = conditional_str[0]
m = conditional_str[1]

graph = [list(map(int, input_data().strip())) for _ in range(n)]


que = deque()
que.append((0,0))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
while que:
	x, y = que.popleft()

	for i in range(4):

		nx = x + dx[i]
		ny = y + dy[i]

		if nx < 0 or ny < 0 or nx >= n  or ny >= m:
			continue
	
		if graph[nx][ny] == 0:
			continue

		if graph[nx][ny] == 1:
			graph[nx][ny] = graph[x][y] + 1
			que.append((nx, ny))

print(graph[n-1][m-1])