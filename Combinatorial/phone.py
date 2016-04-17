def phone(digits, d, prefix=""):
	if len(digits) == 0:
		print prefix 
		return
	else:
		first = d[digits[0]]
		rest = digits[1:]
		for item in first:
			phone(rest, d, prefix+item)
			
# phone dict
d = {
  '2': ['a','b','c'],
  '3': ['d','e','f'],
  '4': ['g','h','i'],
  '5': ['j','k','l'],
  '6': ['m','n','o'],
  '7': ['p','q','r','s'],
  '8': ['t','u','v'],
  '9': ['w','x','y','z'],
}

