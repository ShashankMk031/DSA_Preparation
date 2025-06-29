#Leetcode 19: Remove Nth Node From End of List
"""Given the head of a linked list, remove the nth node from the end of the list and return its head.
Input: head = [1,2,3,4,5], n = 2    
Output: [1,2,3,5]
Example 2:
Input: head = [1], n = 1
Output: []
Example 3:
Input: head = [1,2], n = 1
Output: [1]"""

#Solution: 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # curr = head 
        # num = 0

        # if n == 1:
        #     return None
        # while curr :
        #     num += 1
        #     if num == n:
        #         curr = curr.next.next
        #     else:
        #         curr = curr.next
        #     num += 1
        
        # return head 

        total = 0
        curr = head
        while curr:
            total += 1
            curr = curr.next
        
        target = total -n 

        if target == 0:
            head = head.next
            return head

        curr = head
        count = 0
        while curr:
            if count == target -1:
                curr.next = curr.next.next
                break
            curr = curr.next
            count += 1
    
        return head 
    
    
# Time Complexity: O(n)
# Space Complexity: O(1)
#Above sol is compeltely my approach. 