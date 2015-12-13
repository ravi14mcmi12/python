# program for  Anagram
#imprt sring
from itertools import permutations
#def remove_values_from_list(dupd,common_word):
#	for val in common_word:
#		dupd.remove(word[val])
#	return dupd

with open("sample1.txt", 'r') as f:
	#print(f.read())
#f = open ("sample1.txt", 'r')
	d = [ ]
	i = 0
	text = [word.strip(",.") for line in f for word in line.lower().split()]
	for word in text:
        	#print(f.read())
		if len(word) >= 4 :
			d.append(word)
	#print(d)
	set(d)
#	print(d)
	for word4 in d.copy():
		perms = [''.join(p) for p in permutations(word4)]
		common_word = set(d) & set(perms)
		#common_word = common_word.split()
		#print(common_word)
		if len(common_word) >1:
			sorted(common_word)
			print(", ".join(common_word))
		d = set(d) - set(common_word)
#		remove_values_from_list(dupd, common_word)
		#print(dupd)
			
