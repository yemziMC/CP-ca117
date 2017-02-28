import sys

def main:
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
 '11' : 'eleven',
 '12' : 'twelve',
 '13' : 'thirteen',
 '14' : 'fourteen',
 '15' : 'fifteen',
 '16' : 'sixteen',
 '17' : 'seventeen',
 '18' : 'eighteen',
 '19' : 'nineteen',
 '20' : 'twenty',
 '30' : 'thirty',
 '40' : 'forty',
 '50' : 'fifty',
 '60' : 'sixty',
 '70' : 'seventy',
 '80' : 'eighty',
 '90' : 'ninety',
 '100' : 'one hundred',
 }

def converted(d,t):
	n = t 
	if n in d:
		return d[n]
	tens, units = divmod(n,10)
	return d[tens*10] + '-' + d[units]
if __name__ = 'main':
	main()

 for line in sys.stdin:
 	tokens = line.strip().split()
 	num_list = [converted(d,t) for t in tokens]
 	words = ''.join(num_list)
 print (words)