import sys

def conv2decimal(num,base):
   total = 0
   power = 0
   for c in num[::-1]:
      total += int(c) * base ** power
      power += 1
   return total
print(conv2
