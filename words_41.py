import sys
import string
line = sys.stdin.read().lower().split()

d = {}

for l in line:
	l = l.strip(string.punctuation)

	if l in d:
		d[l] = d[l] + 1
	else:
		d[l] = 1
keys = (sorted(d))
for k in keys:
	print ('{:s} : {:d}'.format(k,d[k]))