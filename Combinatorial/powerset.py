def powerset(n):
	# lists all subsets of n ints
	arr = [None]*(n+1)
	backtrack(arr,0,n)

def isASolution(arr, k, n):
	# stop when k == n
	return k==n

def constructCandidates(candidates):
	# only 2 possibilities at each stage: True or False
	# technically we can just initialise candidates as [True, False] but doing this to follow the tutorial in the Algorithm Design Manual
	candidates.append(True)
	candidates.append(False)

def processSolution(arr, k):
	print "{",
	for i in xrange(1, k+1):
		if arr[i]:
			print str(i),
	print "}"

def backtrack(arr, k, n):
	candidates = []
	num_candidates = 2 #only True or False at each k
	if isASolution(arr, k, n):
		processSolution(arr, k)
	else:
		k += 1
		constructCandidates(candidates)
		for i in xrange(num_candidates):
			arr[k] = candidates[i]
			backtrack(arr, k, n)

print powerset(3)
