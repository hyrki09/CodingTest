import sys

T = int(sys.stdin.readline())
for _ in range(T):
	line = sys.stdin.readline().strip()
	stack = []
	is_valid = True
	for ch in line:
		if ch == '(':
			stack.append('(')
		elif ch == ')':
			if stack:
				stack.pop()
			else:
				is_valid = False
				break
	if stack:
		is_valid = False
	print("YES" if is_valid else "NO")