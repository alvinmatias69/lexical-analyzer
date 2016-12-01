def convert(arr, x):
	i = 0
	error = False

	while (i < len(x)) and (not error):
		if (x[i] == 'p') or (x[i] == 'q') or (x[i] == 'r') or (x[i] == 's'):
			if (i+1 == len(x)) or (x[i+1] == ' ') or (x[i+1] == ')'):
				arr.append(1)
			else: 
				error = True

		elif x[i] == 'n':
			if i + 3 <= len(x):
				if x[i+1] == 'o' and x[i+2] == 't':
					if (i+3 == len(x)) or (x[i+3] == ' ') or (x[i+3] == ')') or (x[i+3] == '('):
						arr.append(2)
						i = i + 2
					else:
						error = True
				else:
					error = True
			else:
				error = True
		
		elif x[i] == 'a':
			if i + 3 <= len(x):
				if x[i+1] == 'n' and x[i+2] == 'd':
					if (i+3 == len(x)) or (x[i+3] == ' ') or (x[i+3] == ')') or (x[i+3] == '('):
						arr.append(3)
						i = i + 2
					else:
						error = True
				else:
					error = True
			else:
				error = True

		elif x[i] == 'o':
			if i + 2 <= len(x):
				if x[i+1] == 'r':
					if (i+2 == len(x)) or (x[i+2] == ' ') or (x[i+2] == ')') or (x[i+2] == '('):
						arr.append(4)
						i = i + 1
					else:
						error = True
				else:
					error = True
			else:
				error = True

		elif x[i] == 'x':
			if i + 3 <= len(x):
				if x[i+1] == 'o' and x[i+2] == 'r':
					if (i+3 == len(x)) or (x[i+3] == ' ') or (x[i+3] == ')') or (x[i+3] == '('):
						arr.append(5)
						i = i + 2
					else:
						error = True
				else:
					error = True
			else:
				error = True

		elif x[i] == 'i':
			if i + 2 <= len(x):
				if x[i+1] == 'f':
					if x[i+2] == 'f':
						if (i+3 == len(x)) or (x[i+3] == ' ') or (x[i+3] == ')') or (x[i+3] == '('):
							arr.append(8)
							i = i + 2
						else:
							error = True
					elif (i+2 == len(x)) or (x[i+2] == ' ') or (x[i+2] == ')') or (x[i+2] == '('):
						arr.append(6)
						i = i + 1
					else:
						error = True
				else:
					error = True
			else:
				error = True

		elif x[i] == 't':
			if i + 4 <= len(x):
				if x[i+1] == 'h' and x[i+2] == 'e' and x[i+3] == 'n':
					if (i+4 == len(x)) or (x[i+4] == ' ') or (x[i+4] == ')') or (x[i+4] == '('):
						arr.append(7)
						i = i + 3
					else:
						error = True
				else:
					error = True
			else:
				error = True	

		elif x[i] == '(':
			arr.append(9)

		elif x[i] == ')':
			arr.append(10)

		elif (x[i] != ' '):
			error = True
		
		i = i + 1

	if error:
		arr.append('error')
	return