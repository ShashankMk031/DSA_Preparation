#Leetcode  876: Middle of the Linked List
"""Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]   
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one."""

#Sokution:
from typing import Optional, List
# Definition for singly-linked list.   
class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
# Time Complexity: O(n)
# Space Complexity: O(1)