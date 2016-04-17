def powerset(lst):
	# generic function for powersets of lists of any sort using recursion

	result = []
	if len(lst) == 0:
		result.append([]) 
	else:
		first, rest = lst[0], lst[1:]
		out = powerset(rest)
		for item in out:
			result.append(item)
			result.append(first+item)
		result 
	return result


	
