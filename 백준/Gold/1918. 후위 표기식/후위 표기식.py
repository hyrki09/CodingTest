import sys

data_str = sys.stdin.readline().strip()

n = len(data_str)

priority = {
	'+' : 1,
	'-' : 1,
	'*' : 2,
	'/' : 2,
	'(' : 0
}

result = []
stack = []


for ch in data_str:
	if ch.isalpha():
		result.append(ch)
	elif ch == "(":
		stack.append(ch)
	elif ch == ")":
		while stack[-1] != "(":
			result.append(stack.pop())
		stack.pop()
	else:
		while stack and priority[stack[-1]] >= priority[ch]:
			result.append(stack.pop())
            
		stack.append(ch)

while stack:
	result.append(stack.pop())
    

print(''.join(result))

		