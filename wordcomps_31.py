import sys
a = []
def allvowels(l):
	l = l.lower()
	if "a" in l and "o" in l and "e" in l and "i" in l and "u" in l:
		return True
for line in sys.stdin:
	a.append(line.strip())
	
print('Words containing 17 letters:',[l for l in a if len(l) == 17])
print('Words containing 18+ letters:',[l for l in a if len(l) >= 18])
vowelwords = [l for l in a if allvowels(l)]
print('Shortest word containing all vowels:',min(vowelwords,key=len)) 
print("Words with 4 a's:",[l for l in a if l.lower().count('a') == 4])
print("Words with 2+ q's:",[l for l in a if l.lower().count('q') >= 2])
print("Words containing cie:",[l for l in a if l.lower().count('cie') >= 1])
print('Anagrams of angle:',[l for l in a if sorted(l.lower()) == sorted('angle') if l.lower() != 'angle'])
print('Words ending in iary:',len([l for l in a if len(l) >= 4 and l.lower()[-4:] == 'iary']))
print('Words with q but no u:', [l for l in a if "q" in l.lower() if "qu" not in l.lower()])
ecount = [l.lower().count("e") for l in a if "e" in l]
emax = max(ecount)
print("Words with most e's:",[l for l in a if l.lower().count("e") == emax])













