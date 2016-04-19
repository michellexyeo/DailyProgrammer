# Hackerrank knapsack problem: https://www.hackerrank.com/challenges/unbounded-knapsack/submissions/code/19430251
num_cases = int(raw_input())
for _ in xrange(num_cases):
    n, k = map(int, raw_input().strip().split())
    A = map(int, raw_input().strip().split())
    
    max_sum = [0]*(k+1)
    for i in xrange(1,n+1):
        for j in xrange(1,k+1):
            if j >= A[i-1]:
                max_sum[j] = max(max_sum[j], max_sum[j-A[i-1]]+A[i-1])
    print max_sum[-1]
