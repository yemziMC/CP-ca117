import sys
d = {
'0' : 'zero',
'1' : 'one',
'2' : 'two',
'3' : 'three',
'4' : 'four',
'5' : 'five',
'6' : 'six',
'7' : 'seven',
'8' : 'eight',
'9' : 'nine',
'10' : 'ten',
}

for line in sys.stdin:
	a = []
	line = line.strip().split()
	for num in line:
		if num in d :
			a.append(d[num])
		else:
			a.append('unknown')
	print(" ".join(a))