771. Jewels and Stones 


You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0 

# Solution :  

# Using HashMap method 
        stone_counts = Counter(stones)
        return sum(stone_counts[jewel] for jewel in jewels)   
        
    #If you don't want to use Counter: 
        jewel_set = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1 
        return count
        
#Time complexity: O(m +n )
#Space complexity: O(n)
        
# Using Brute force method
        count = 0
        for stone in stones:
            if stone in jewels:
                count = count + 1 
        return count 

#Time complexity: O(n * m )
#Space complexity: O(1)   