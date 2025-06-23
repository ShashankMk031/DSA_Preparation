#Leetcode 206 : Reverse Linked List
"""Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Input: head = [1,2]
Output: [2,1]"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None  # Initialize prev as None
        curr = head  # Start with curr at the head of the list

        while curr:
            temp = curr.next  # Store the next node
            curr.next = prev  # Reverse the pointer
            prev = curr       # Move prev forward
            curr = temp      # Move curr forward

        return prev  # prev is the new head of the reversed list 
    
    # Time Complexity: O(n) where n is the number of nodes in the linked list
    # Space Complexity: O(1) as we are not using any extra space except for the pointers
    # The above code reverses the linked list in place without using any extra space
    # The code iterates through the linked list and reverses the pointers of each node.
    # It uses three pointers: prev, curr, and temp.
    # - prev starts as None, curr starts at the head of the list, and temp is used to temporarily store the next node.
    # - In each iteration, it reverses the pointer of the current node to point to the previous node.
    # - It then moves prev to the current node and curr to the next node (stored in temp).
    # - This continues until curr becomes None, at which point prev will be pointing to the new head of the reversed list.      