import sys
import re

# input_data = sys.stdin.read().split('.')
# input_data.pop()
# input_data = [str.strip() for str in input_data ]

pairs = {')' : '(', ']' : '['}
for line in sys.stdin:
	line = line.rstrip()
	if line == '.':
		break
	removed_str = re.sub(r"[^()\[\]]", "", line)
	
	stack = []
	isSuccess = True


	if removed_str:
		for i in removed_str:
			if i in '([':
				stack.append(i)
			else:
				if not stack or stack[-1] != pairs[i]:
					isSuccess = False
					break
				else:
					stack.pop()
	print('yes') if isSuccess and not stack else print('no')