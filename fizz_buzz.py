#Charlie Miller
#Leetcode - 412. Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        Classic problem B)
        Goal here is maxiumum extendability
        Store all divisors and corresponding word e.g 3 -> Fizz in a map
        check each divisor with a modulo, and append the word when we find it's a multiple
        """
        
        #init output
        output = [None] * n
        
        #words map defined here. IRL should be in a configurable file
        words = {
            3:"Fizz",
            5:"Buzz"
        }
        
        for num in range(1,n+1):
            
            #init answer builder
            cur_ans = ""
            
            #iterate over each divisor and add associated word if we find match
            for divisor,word in words.items():
                if num % divisor == 0:
                    cur_ans += word
                    
            # Case when there's no match, just use the number
            if cur_ans == "":
                cur_ans = str(num)
                
            output[num-1] = cur_ans
            
        return output