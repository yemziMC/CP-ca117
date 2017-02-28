import sys
for line in sys.stdin:
   line = line.strip()
   n = ''
   for c in line:
      if c.isalpha():
      	n = n + c.lower()
   print (n == n[::-1])

