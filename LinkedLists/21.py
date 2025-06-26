#Leetcode 21 : Merge Two Sorted Lists
"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""

#Solution: 
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # head1 = list1
        # head2 = list2
        # while head1:
        #     head1 = head1.next
        #     if head1.next == None:
        #         head1.next = head2
        #     # The link is established.

        #     if head1.val < head1.next.val :
        #         head1.val.next = head1.next.val.next
        #         head1.next.val =  
        """Above method will go for like O(1) in space compelxity and the code for sorting is complex"""
        d = ListNode()
        curr = d

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next 
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next

        curr.next = list1 if list1 else list2

        return d.next 
# Time Complexity: O(n + m) where n is the number of nodes in list1 and m is the number of nodes in list2
# Space Complexity: O(1) as we are not using any extra space except for the pointers
# The above code merges two sorted linked lists into one sorted linked list in a single pass
# The code uses a dummy node to simplify the merging process. It iterates through both lists
# and compares the values of the current nodes in both lists. The smaller value is added to
# the merged list, and the pointer for that list is moved to the next node. This continues until one of the lists is exhausted. 
# Finally, the remaining nodes from the non-exhausted list are appended to the merged list. 
# The function returns the head of the merged linked list, which is the next node of the dummy node.
# This approach ensures that the merged linked list is sorted and constructed in a single pass through both input lists, maintaining O(n + m) time complexity and O(1) space complexity.  