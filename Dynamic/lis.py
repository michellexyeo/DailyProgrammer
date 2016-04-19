# longest increasing subsequence
# problem from hackerrank: https://www.hackerrank.com/challenges/longest-increasing-subsequent/submissions/code/19429256

# L(i) = { 1 + Max ( L(j) ) } where j < i and arr[j] < arr[i] and if there is no such j then L(i) = 1
# using this: http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/

n = int(raw_input())
seq = []
for _ in xrange(n):
    seq.append(int(raw_input()))

sol = [1]*n
for i in xrange(1, n):
    for j in xrange(0, i):
        # need to check if 
        # 1) current int is larger than prev int
        # 2) if longest subsequence from prev int yields a better solution than that for the current (so we set the current subsequence to go through the prev one)
        if seq[i] > seq[j] and sol[j] >= sol[i]:
            sol[i] = sol[j] + 1 # add one due to the fact that seq[i] > seq[j]
print max(sol)

