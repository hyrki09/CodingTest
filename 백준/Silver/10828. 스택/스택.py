import sys

T = int(sys.stdin.readline())

stack = []
for _ in range(T):
	req_str = sys.stdin.readline().strip().split()
	
	command_line = req_str[0]
	if command_line == 'push':
		stack.append(req_str[1])
	elif command_line == 'top':
		print(stack[-1] if len(stack) != 0 else -1)
	elif command_line == 'size':
		print(len(stack))
	elif command_line == 'empty':
		print(1 if not stack else 0)
	elif command_line == 'pop':
		print(stack.pop() if stack else -1)