import sys
for line in sys.stdin:
   line = line.strip().split()
   a = line[0]
   b = line[1]
   print(sorted(a) == sorted(b))