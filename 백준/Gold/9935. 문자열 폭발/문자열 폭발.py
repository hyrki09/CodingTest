import sys

input = sys.stdin.readline

data_str = input().strip()
boom_str = input().strip()

n = len(data_str)
boom_n = len(boom_str)



stack = []

for i in data_str:
	stack.append(i)

	if len(stack) >=boom_n:
		if ''.join(stack[-boom_n:]) == boom_str:
			for _ in range(boom_n):
				stack.pop()

print(''.join(stack) if stack else 'FRULA')





