# Leetcode 20: Valid Parentheses
"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true"""


# Solution:

class Solution:
    def isValid(self, s: str) -> bool:
        # if s.count("(") == s.count(")") and s.count("{") == s.count("}") and s.count("[") == s.count("]") :
        #     return True
        # return False 
        """It won't  work work cause the order of the brackets should be same """

        #Hashmaps sol

        mapp = {")" : "(", ']' : '[', '}' : '{'}

        stack = [] 

        for c in s :
            if c not in mapp:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    poped = stack.pop()
                    if poped not in mapp[c]:
                        return False
        return len(stack) == 0
    
# Time Complexity : O(n)
# Space Complexity : O(n)