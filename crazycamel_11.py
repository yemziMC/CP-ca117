import sys
s = sys.stdin.readline()

while len(s)>0:
	t = []
	for c in s.split():
	   t.append(c[0:-1]+c[-1].upper())
	print(' '.join(t))
	s = sys.stdin.readline()
   
