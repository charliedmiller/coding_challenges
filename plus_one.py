# Charlie Miller
# Leetcode - 66. Plus One
# https://leetcode.com/problems/plus-one/
# Written 4/20/2020

"""
Convert array to number, add, then recreate
array
"""

class Solution:
    def convert_to_number(self,arr):
        #add each digit, shift left base 10 for each 
        #new number
        arr.reverse()
        number = 0
        for i,digit in enumerate(arr):
            value = digit * (10 ** i)
            number += value
            
        return number
        
    def convert_to_list(self,number):
        #create a string representing the number
        #then convert each character to the digit
        string = str(number)
        arr = [digit for digit in string]
        arr = list(map(int,arr))
        return arr
        
    def plusOne(self, digits: List[int]) -> List[int]:
        value = self.convert_to_number(digits)
        value += 1
        new_arr = self.convert_to_list(value)
        return new_arr