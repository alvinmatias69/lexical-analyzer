from tahap1 import convert

def validate(x):
	arr = []
	stack = []
	state = ''

	convert(arr, x.lower())
	if arr[-1] == 'error':
		print(arr[-1])
	else:
		stack.append('#')
		state = 'q1'
		# print(arr)
		for x in range(len(arr)):
			if state == 'q1':
				if arr[x] == 1:
					state = 'q2'
				elif arr[x] == 9:
					stack.append('9')
				elif arr[x] == 6:
					stack.append('6')
				else:
					stack.append('err')
			elif state == 'q2':
				if arr[x] == 1:
					stack.append('1')
				elif arr[x] == 10 and stack[-1] == '9':
					stack.pop()
				elif arr[x] == 7 and stack[-1] == '6':
					stack.pop()
					state = 'q1'
				elif arr[x] == 3 or arr[x] == 4 or arr[x] == 5 or arr[x] == 8:
					state = 'q1'
			if x == len(arr) - 1 and stack[-1] == '#':
				state = 'qx'
				stack.pop()
		if len(stack) == 0 and state == 'qx':
			return 'valid'
		else:
			return 'tidak valid'
				
x = str(input("input string "))
print(validate(x))
