import sys
from collections import deque

input_str= sys.stdin.readline().strip()
input_list = input_str.split()
N = (int) (input_list[0])
M = (int) (input_list[1])
V = (int) (input_list[2])

line = [[] for _ in range(N+1)]

for _ in range(M):	
	m= list(map(int, sys.stdin.readline().strip().split()))
	line[m[0]].append(m[1])
	line[m[1]].append(m[0])

for sub in line:
	sub.sort()

que = deque([V])

dfs_visited = [False] * (N+1)
dfs_visited[V] = True
dfs_list = [V]
bfs_visited = [False] * (N+1)
bfs_visited[V] = True
bfs = [V]


def dfs(v,  visited):
	visited[v] = True
	for j in line[v]:
		if not visited[j]:
			dfs_list.append(j)
			dfs(j, visited)

dfs(V,dfs_visited)

que = deque([V])
while que:
	idx = que.popleft()
	for i in line[idx]:
		if not bfs_visited[i]:
			bfs_visited[i]= True
			que.append(i)
			bfs.append(i)




print(' '.join(list(map(str, dfs_list))))
print(' '.join(list(map(str, bfs))))