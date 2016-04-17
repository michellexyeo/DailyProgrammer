def anagrams(s, prefix = ''):
	# returns all the anagrams of the given string
	if len(s) == 0:
		return prefix 
	else:
		tmp = []
		# choose first letter and recurse on remainder
		for i in xrange(len(s)):
			tmp.append(anagrams(s[:i]+s[i+1:], prefix+s[i]))
		return tmp
		
print anagrams("abc")

