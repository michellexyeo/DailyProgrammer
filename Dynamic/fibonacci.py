# modified fib from hackerrank
# https://www.hackerrank.com/challenges/fibonacci-modified

a, b, n = map(int,raw_input().strip().split())
for _ in xrange(3, n+1):
    c = b**2 + a
    a, b = b, c
print c
