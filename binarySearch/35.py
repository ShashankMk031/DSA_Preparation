#Leetcode 35: Search Insert Position
"""Given a sorted array of distinct integers and a target value, return the index if the target
is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
Input: nums = [1,3,5,6], target = 5
Output: 2"""

#Solution :
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left  # The position where the target should be inserted.
# Time Complexity: O(log n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are using a constant amount of space for the pointers.
# The algorithm uses binary search to find the target or the position where it should be inserted.
# If the target is not found, the left pointer will indicate the correct insertion position.    

#Sol 2:
class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        
        return len(nums)  # If target is greater than all elements, return the length of the array
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are using a constant amount of space for the loop variable.
# This solution iterates through the array to find the first position where the target can be inserted.
# If the target is greater than all elements, it returns the length of the array
# as the insertion position.    