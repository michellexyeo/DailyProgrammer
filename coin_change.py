# Hackerrank coin change problem: https://www.hackerrank.com/challenges/coin-change
# Enter your code here. Read input from STDIN. Print output to STDOUT
# using this: http://www.ideserve.co.in/learn/coin-change-problem-number-of-ways-to-make-change
n, m = map(int, raw_input().strip().split())
coins = map(int, raw_input().strip().split())

# base case: n = 0
sol = [0]*(n+1)
sol[0] = 1 

for i in xrange(1, m+1): # for each coin
    for j in xrange(1, n+1): # range of change
        if j >= coins[i-1]:
            sol[j] += sol[j-coins[i-1]]
print sol[-1]
