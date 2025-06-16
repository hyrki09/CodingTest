import sys

left_stack = list(sys.stdin.readline().strip())
right_stack = []

n = int(sys.stdin.readline())

for _ in range(n):
	command_str = sys.stdin.readline().strip()

	if command_str == 'L':
		if left_stack:
			right_stack.append(left_stack.pop())
	elif command_str == 'D':
		if right_stack:
			left_stack.append(right_stack.pop())
	elif command_str == 'B':
		if left_stack:
			left_stack.pop()
	elif 'P' in command_str:
		left_stack.append(command_str[-1])

print(''.join(left_stack + list(reversed(right_stack))))