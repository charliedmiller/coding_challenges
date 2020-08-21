# Charlie Miller
# Leetcode - 824. Goat Latin
# https://leetcode.com/problems/goat-latin/

class Solution:
    def toGoatLatin(self, S: str) -> str:
        new_sentence = ""
        words = S.split()
        vowels = "aeiouAEIOU"
        
        for a_ctr,word in enumerate(words):
            goat_word = word
            
            #apply vowel rule
            if word[0] in vowels:
                goat_word = word + "ma"
            else:
                goat_word = word[1:] + word[0] + "ma"
                
            #apply 'a' rule
            goat_word += "a" * (a_ctr+1)
            
            new_sentence += goat_word + " "

        # last word has an unecessary space
        return new_sentence[:-1]
                