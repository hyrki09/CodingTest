
import sys


n = int(sys.stdin.readline())

stack = []
stack_log = []
start_num = 1
isStop = False;
for i in range(1, n+1):
	param_num = int(sys.stdin.readline())
	# print("명령 : ", param_num)
	if not stack or stack[-1] < param_num:
		if start_num <= param_num:        
			stack += [j for j in range(start_num, param_num + 1)]
			stack_log += ['+' for _ in range(start_num, param_num + 1)]
			start_num = param_num + 1
		else:
			isStop = True
			break;
	elif stack[-1] > param_num:
		# print('빼기전 : ' ,stack)
		if param_num in stack:
			s = stack.index(stack[-1])
			e = stack.index(param_num)
			for _ in range(s - e):
				stack.pop()
				stack_log.append('-')
		else:
			isStop = True
			break;
            
	stack_log.append('-')
	stack.pop()
	# print(stack_log)
	# print(stack)
#	print("출력 : ", stack.pop())

if isStop:
	print('NO')
else:	
	stack_log.reverse()
	while stack_log:
		print(stack_log.pop())