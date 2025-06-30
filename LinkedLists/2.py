# Leetcode 2 : # Add Two Numbers
"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]"""

# Solution:
from typing import Optional, List 

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # curr1 = l1
        # curr2 = l2
        # curr1val = 0
        # curr2val = 0

        # while curr1:
        #     curr1val += curr1.val
        #     curr1 = curr1.next 
                                            #Didn't consider carry , My bad
        # while curr2:
        #     curr2val += curr2.val
        #     curr2 = curr2.next
        # res = curr1val + curr2val 
        # return ListNode(res)
        dummy = ListNode() 
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
        return dummy.next 
    
# Time Complexity: O(max(m, n)), where m and n are the lengths of the two linked lists.
# Space Complexity: O(max(m, n)), for the new linked list that is created to store the result.
# The space complexity is O(1) if we consider the output linked list as part of the input, but typically we consider the space used for the output separately.

#Solution 2: Using Recursion
class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addNodes(n1, n2, carry):
            if not n1 and not n2 and carry == 0:
                return None
            
            val = carry
            if n1:
                val += n1.val
                n1 = n1.next
            if n2:
                val += n2.val
                n2 = n2.next
            
            carry = val // 10
            node = ListNode(val % 10)
            node.next = addNodes(n1, n2, carry)
            return node
        
        return addNodes(l1, l2, 0) 
    
# Time Complexity: O(max(m, n)), where m and n are the lengths of the two linked lists.
# Space Complexity: O(max(m, n)), for the recursion stack and the new linked listthat is created to store the result.
# The space complexity is O(1) if we consider the output linked list as part of the input, but typically we consider the space used for the output separately.

