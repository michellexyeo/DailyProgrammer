# Enter your code here. Read input from STDIN. Print output to STDOUT
# Python code mainly taken from here: http://www.algorithmist.com/index.php/Longest_Common_Subsequence
len1, len2 = map(int, raw_input().strip().split())
seq1 = map(int, raw_input().strip().split())
seq2 = map(int, raw_input().strip().split())

M = dict() # used as 2d array with M[i,j] = longest common subsequence at seq1[:i] and seq2[:j]
for i in xrange(len1):
    for j in xrange(len2):
        # fill up the first row and col with zeroes since lcs with one string being 0 length is 0
        if i == 0 or j == 0:
            M[i, j] = 0
        # now to compare the values in the sequence. if the values at each step (i,j) are the same, add 1 to the length of the i-1th and j-1th step. if they're different, the lcs must be the max of the (i-1,j) and (i,j-1) steps as thats the value of the lcs we get by deleting a char in either direction
        else:
            if seq1[i] == seq2[j]:
                M[i,j] = 1 + M[i-1,j-1]
            else:
                M[i,j] = max(M[i-1,j], M[i,j-1])
                
# reconstructing the subsequence
sol = []
i, j = 0, 0
while (i < len1) and (j < len2):
    if seq1[i] == seq2[j]:
        sol.append(seq1[i])
        i += 1
        j += 1
    else:
        # increment in direction which will give a longer lcs
        if M[i+1, j] >= M[i, j+1]:
            i += 1
        else:
            j += 1

for i in sol:  
    print i
        
            
           
        
        
       
