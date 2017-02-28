import sys

def main():
 m = {}
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
 with open(sys.argv[1], 'r' ) as f:
 	for line in f:
 		[key,value] = line.strip().split()
 		m[key] = value
    for line in sys.stdin:
 	    tokens = line.strip().split()
 		num_list = [m[d[t]] for t in tokens]
 		words = ''.join(num_list)
 		print (words)
if __name__ == 'main':
	main()