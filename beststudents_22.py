import sys
try:
	with open(sys.argv[1],'r') as f:
		h_result = 0
		b_student = []
		d = {}
		names = []
		for line in f:
			line = line.strip().split()
			d[' '.join(line[1:])] = line[0]
			names.append(' '.join(line[1:]))
		maximum = max(d.values())
		for name in names :
			if d[name] == maximum:
				b_student.append(name)
		print ( 'Best student(s):',', '.join(b_student))
		print ('Best mark:',max(d.values()))


except FileNotFoundError:
	print ('File does not exist')