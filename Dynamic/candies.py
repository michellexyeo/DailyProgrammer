# solution to hackerrank candies problem: https://www.hackerrank.com/challenges/candies

n = int(raw_input())
ratings = []
for _ in xrange(n):
    ratings.append(int(raw_input()))

candies = [1]*n
# check to see if ratings of person to the right is larger
for i in xrange(1, n):
    if ratings[i-1] < ratings[i]:
        candies[i] = candies[i-1] + 1
        
# check to see if ratings of person to the left is larger
for i in xrange(n-2, -1, -1):
    if ratings[i+1] < ratings[i]:
        # check if person on the left already has more than enough candies
		# i.e. candies[i] > candies[i+1]+1
        candies[i] = max(candies[i], candies[i+1]+1)
        
print sum(candies)
