import sys
from collections import deque

input_data = sys.stdin.readline

size_list = input_data().strip().split()

M = int (size_list[0])
N = int (size_list[1])

visited = [[False] * M for _ in range(N)]
graph = []
for data in range(N):
	graph.append(list(map(int, input_data().strip().split())))


dx = [1,0,-1,0]
dy = [0,1,0,-1]

que = deque()
for i in range(N):
	for j in range(M):
		if graph[i][j] == 1 and not visited[i][j]:
			count = 0
			visited[i][j] = True
			que.append((i,j))
			
while que:
	y,x = que.popleft()
				
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0<=nx<M and 0<= ny < N:
			if graph[ny][nx] == 0 and not visited[ny][nx]:
				graph[ny][nx] = graph[y][x] + 1
				que.append((ny,nx))
				visited[ny][nx] = True


result = 0
for row in graph:
	if 0 in row:
		print(-1)
		exit()
	result = max(result, max(row))

print(result - 1)
	