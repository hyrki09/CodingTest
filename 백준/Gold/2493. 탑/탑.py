import sys

input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))

stack = []
reception = [0] * n

for i in reversed(range(n)):
	while stack and tower[stack[-1]] < tower[i]:
		index = stack.pop()
		reception[index] = i + 1
	
	stack.append(i)

print(' '.join(map(str, reception)))
	

