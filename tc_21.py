import sys
total = 0
for line in sys.stdin:
	line = line.strip().split()
	total = total + (len(line))
print (total)

print('Words containing 17 letters:')
print('Words containing 18+ letters:') 
print('Shortest word containing all vowels:') 
print(" Words with 4 a's:")
print("Words with 2+ q's:")
print('Words containing cie:')
print('Anagrams of angle:')
print('Words ending in iary: 14')
print("Words with q but no u:")
print("Words with most e's")