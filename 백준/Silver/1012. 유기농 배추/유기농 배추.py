import sys
from collections import deque

input_str= sys.stdin.readline
T = int(input_str().strip())

dx = [-1, 0 ,1 ,0]
dy = [0, -1, 0, 1]
result = []
for _ in range(T):
	option_list = list(map(int, input_str().strip().split()))
	M = option_list[0]
	N = option_list[1]
	K = option_list[2]

	graph = [[0] * M for _ in range(N) ]
	visited = [[False] * M for _ in range(N)]
    
	for _ in range(K):
		baechu_pos = list(map(int, input_str().strip().split()))
		graph[baechu_pos[1]][baechu_pos[0]] = 1

	# result = []
	cnt = 0
	for i in range(N):
		for j in range(M):
			if graph[i][j] == 1 and not visited[i][j]:
				que = deque([(i,j)])
				visited[i][j] = True
				# cnt = 0
				while que:
					x,y = que.popleft()
					for k in range(4):
					
						nx = x + dx[k]
						ny = y + dy[k]
						if 0<= nx < N and 0<= ny <M:
							if graph[nx][ny] == 1 and not visited[nx][ny]:
								visited[nx][ny] = True
								que.append([nx,ny])
				cnt += 1
	print(cnt)