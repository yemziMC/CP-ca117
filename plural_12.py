import sys
line = sys.stdin.read().strip().split('\n')
vowels = ['a','e','i','o','u']
i = 0

for lines in line:
   
   if lines[-2:] == 'ch' or lines[-2:] == 'sh' or lines[-1:] == 'x' or lines[-1:] == 's' or lines[-1:] == 'z':
      lines += 'es'
   elif lines[-2] not in vowels and lines[-1] == 'y':
     lines = lines.replace(lines[-1], 'ies')
   elif lines[-2:] == 'fe':
     lines = lines.replace('fe','ves') 
   elif lines[-1] == 'f':
     lines = lines.replace('f','ves')
   elif lines[-1] == 'o':
      lines += 'es'
   else:
      lines += 's'
   print (lines)
