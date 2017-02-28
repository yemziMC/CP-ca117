import sys
import string
total = 0
words = []
for line in sys.stdin:
	line = line.strip()
	n = ''
	line = line.lower()
	for c in line:
		if c in string.punctuation:
			line = line.replace(c, '')
	line = line.split()
	print(len(line))
