#Problem Statement 
# Merge Strings Alternately
#ou are given two strings word1 and word2. Merge the strings by adding letters 
#in alternating order, starting with word1. If a string is longer than the other,
# append the additional letters onto the end of the merged string.

#Example 1:
#Input: word1 = "abc", word2 = "pqr"
#Output: "apbqcr" 

#Example 3:
#Input: word1 = "abcd", word2 = "pq"
#Output: "apbqcd"

form collections import deque 

q1 = deque(word1)
q2 = deque(word2)
result = []

while q1 or q2:
    if q1:
        result.append(q1.popleft())
        
    if q2:
        result.append(q2.poplest())
        
merge = ''.join(result)
return merge