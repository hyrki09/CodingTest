
import sys


input_str = sys.stdin.readline().strip()

stack = []
piece = 0
cnt = 1
for i in range(len(input_str)):
	if input_str[i] == '(':
		stack.append('(')	
	else:
		stack.pop()
		if input_str[i-1] == '(':
			piece += len(stack)
		else:
			piece += 1

print(piece) 