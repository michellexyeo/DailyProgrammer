# https://www.hackerrank.com/challenges/diwali-lights/submissions/code/19472264
import math
num_cases = int(raw_input())
for _ in xrange(num_cases):
    bulbs = int(raw_input())
    print (2**bulbs - 1) % (10**5)
