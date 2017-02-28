import sys

f = sys.argv[1]

d = {}

with open(f,'r') as f:

	for line in f:
		[name,number] = line.split()
		d[name] = number

names = sys.stdin.readlines()

for name in names:

	name = name.rstrip()

	if name in d:
		print('Name: {:s}\nPhone: {:s}'.format(name,d[name]))
	else:
		print('Name: {:s}\nNo such contact'.format(name))


