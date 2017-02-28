import sys
lines = sys.stdin.read().strip().split('\n')

i = 0
while i < len(lines):

   digit = 0
   lower = 0
   upper = 0
   other = 0

   line = lines[i]
   j = 0
   while j < len(line):
   
      if line[j].isdigit():
         digit = 1
      elif line[j].islower():
         lower = 1
      elif line[j].isupper():
         upper = 1
      else:
         other = 1
      j += 1

   print (digit + upper + lower + other )
   i += 1          
      
