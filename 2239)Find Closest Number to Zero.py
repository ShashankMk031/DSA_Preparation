# Problem statement
# Given an integer array nums of size n, return the number with the value closest to 0 in nums.
# If there are multiple answers, return the number with the largest value.

#Example 1 :
#Input: nums = [-4, -2, -1, 1,3]
#Output : 1 

#Example 2:
#Input : nums = [-2,4,5]
#Output : 2

closest = nums[0]

for x in nums:
    if x < abs(closest):
        closest = x

if closest < x and abs(closest) in nums:
    return abs(closest)

else:
    return closest