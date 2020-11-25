# Charlie Miller
# Leetcode - 227. Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/
# Written 2020-11-24

"""
parse the string into numbers and operators
Calculate * and / in left right order, then
+ and - to preserve pemdas. To calculate, maintain
an accumulator, perform operations on it according 
to the next operator, and the next number. During the
* / phase also output to a new numbers and operators 
array if the value/operator need to be preserved for
the + - phase.
To add parenthesis, simply extract the expressions in them
recursively, then use this routine to perform the real calculation
"""

class Solution:
    def get_numbers(self,s):
        s = s.replace("+"," ")
        s = s.replace("-"," ")
        s = s.replace("/"," ")
        s = s.replace("*"," ")
        numbers = [int(num) for num in s.split()]
        return numbers
    
    def get_ops(self,s):
        return [op for op in list(s) if op in ["+","-","*","/"]]
    
    def calculate(self, s: str) -> int:
        #get numbers and operators arrays
        numbers = self.get_numbers(s)
        operators = self.get_ops(s)
        
        #edgecase: nothing is brought in        
        if not numbers:
            return 0
        
        #start accumulator, and arrays to use for + - phase
        cur_num = numbers[0]
        new_numbers = []
        new_operators = []
        for op,num in zip(operators,numbers[1:]):
            if op == "*":
                cur_num *= num
            elif op == "/":
                cur_num //= num
            else:
                #expression to the left has been simplified as much
                #as possible, and we're not doing the operation specified
                #now until all * / has been completed Add both to the
                #new arrays.
                new_numbers.append(cur_num)
                new_operators.append(op)
                #start the accumulator with our most recent number
                cur_num = num
        
        #add whatever was accumulated to + - as cleanup
        new_numbers.append(cur_num)

        #new accumulator is just the result. Go left to right
        result = new_numbers[0]
        for op,num in zip(new_operators,new_numbers[1:]):
            if op == "+":
                result += num
            elif op == "-":
                result -= num
            else:
                #invalid operator somehow got in
                print("invalid operator!!")
                
        return result
        
        
                