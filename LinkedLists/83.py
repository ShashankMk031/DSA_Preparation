#Leetcode 83 : Remove Duplicates from Sorted List
"""Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
Input: head = [1,1,2]
Output: [1,2]
Input: head = [1,1,2,3,3]
Output: [1,2,3] """

#Solution : 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """   curr = head 
        res = []
        while curr:
            if curr.val not in res:
                res.append(curr.val)
            curr = curr.next 
        
        return res 


        I   got the answer in the above method , but it is wrong because the return type should be a ListNode , I am getting it in List even though the answer is correct """ 
        # Now the ListNode approach:  
        # Given the nodes that are duplicates only appear once that is twice is max and are sorted 
        curr = head 

        while curr and curr.next:
            if curr.val  == curr.next.val :
                curr.next = curr.next.next
            else :
                curr = curr.next 
        return head 
    
    
    
# Time Complexity : O(n) where n is the number of nodes in the linked list
# Space Complexity : O(1) as we are not using any extra space except for the pointers
# The above code is a single pass solution that removes duplicates in place without using any extra space.
# The code iterates through the linked list and checks if the current node's value is equal to the next node's value. If they are equal, it skips the next node by updating the current node's next pointer to point to the node after the next node. If they are not equal, it simply moves to the next node. This way, all duplicates are removed in a single pass through the linked list. The function returns the head of the modified linked list with duplicates removed.