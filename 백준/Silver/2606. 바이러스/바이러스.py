import sys
from collections import deque

input_str= sys.stdin.readline
computer_count = (int)(input_str().strip())
n = (int)(input_str().strip())

graph = [[] for _ in range(computer_count + 1)]
bfs_visited = [False] * (computer_count+1)

for i in range(n):
	
	link_list = list(map(int, input_str().split()))
	a = link_list[0]
	b = link_list[1]
	graph[a].append(b)
	graph[b].append(a)

que = deque([1])
bfs_visited[1] = True

while que:
	idx = que.popleft()

	for i in range(len(graph[idx])):
		c = graph[idx][i]
		# print(c)
		# print(bfs_visited[c])
		if not bfs_visited[c]:
			que.append(c)
			bfs_visited[c] = True

print(bfs_visited.count(True)-1)


