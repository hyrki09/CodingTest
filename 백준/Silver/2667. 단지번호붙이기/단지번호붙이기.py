import sys
sys.setrecursionlimit(10000)

input_str= sys.stdin.readline
n = (int)(input_str().strip())

graph = []
for i in range(n):
	graph.append(list(map(int, input_str().strip())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

visited = [[False] * n for _ in range(n)]


def dfs(x, y):
	visited[x][y] = True
	cnt = 1

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0 <= nx < n and 0 <= ny < n:
			if graph[nx][ny] == 1 and not visited[nx][ny]:
				cnt += dfs(nx,ny)
				
	return cnt
	
result = []
for j in range(n):
	for k in range(n):
		if graph[j][k] == 1 and not visited[j][k]:			
			result.append(dfs(j,k))

result.sort() 


print(len(result))
for i in result:
	print(i)



# print(dfs(1,0))

