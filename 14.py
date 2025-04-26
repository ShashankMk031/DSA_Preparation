
Code
Code
Code Sample
Testcase
Testcase
Test Result
14. Longest Common Prefix
Solved
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings. 


#Solution 

        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
            if prefix == "":
                return ""
        
        if not strs:
            return ""
        return prefix 
    

#Time Complexity : O(n * m2)
#Space complexity : O(m)