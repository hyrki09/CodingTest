import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

stack = []
nge = [-1] * n
for i in range(n):
	while stack and num_list[stack[-1]] < num_list[i]:
		index = stack.pop()
		nge[index] = num_list[i]
        
	stack.append(i)

print(' '.join(map(str, nge)))