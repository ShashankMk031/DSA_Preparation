# Leetcode 977: Squares of a Sorted Array

"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]"""


#Solution 1 : 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        return sorted(nums)
    
    
#Time Complexity : O(nlogn)
#Space Complexity : O(1)
#Solution 2 : Two Pointers
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
                
        return result
#Time Complexity : O(n)
#Space Complexity : O(n)
#Solution 3 : Using List Comprehension
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x ** 2 for x in nums])
#Time Complexity : O(nlogn)
#Space Complexity : O(n)
#Solution 4 : Using Map Function
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(map(lambda x: x ** 2, nums))
#Time Complexity : O(nlogn)
#Space Complexity : O(n)