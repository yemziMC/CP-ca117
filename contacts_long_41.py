import sys

f = sys.argv[1]

d = {}

with open(f,'r') as f:

	for line in f:
		[name,number,email] = line.split()
		d[name] = (number, email)


names = sys.stdin.readlines()

for name in names:

	name = name.rstrip()

	if name in d:
		print('Name: {:s}\nPhone: {:s}\nEmail: {:s}'.format(name,d[name][0],d[name][1]))
	else:
		print('Name: {:s}\nNo such contact'.format(name))