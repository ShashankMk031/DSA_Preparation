#Problem Statement 
Roman to integer 

Given a roman numeral, convert it to an integer. 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


#code ;  

 values = {'I':1, 'V':5 , 'X' : 10, 'L' : 50, 'C':100, 'D': 500, 'M': 1000}
         total = 0
         prev_value = 0
         for char in reversed(s):
             curr_value = values[char]
             if curr_value< prev_value:
                 total -= curr_value
             else:
                 total += curr_value
                 prev_value = curr_value
         return total 
     
     
Create a dictionary that holds all the values . then create a total/summ that adds , iterate through the string 
In this case it is reversed string , comapre the values in i and i-1 positions if they are lesser than subtract them from the 
total else add them to total and update the values after each iteration. 

Time Complexity : O(n)
Space COmplexity : O(1)