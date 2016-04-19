# https://www.hackerrank.com/challenges/summing-the-n-series/submissions/code/19471951
import math
num_cases = int(raw_input())
for _ in xrange(num_cases):
    n = int(raw_input())
    print n*n % (10**9 + 7)
