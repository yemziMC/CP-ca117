import sys
try:
	with open(sys.argv[1],'r') as f:
		h_result = 0
		b_student = 0
		for line in f:
			line = line.strip().split()
			if int(line[0]) > h_result:
				h_result = int(line[0])
				b_student = line[1:]
		print ( 'Best student:',' '.join(b_student))
		print ('Best mark:',h_result )


except FileNotFoundError:
	print ('File does not exist')