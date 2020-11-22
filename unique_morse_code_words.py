# Charlie Miller
# Leetcode - 804. Unique Morse Code Words
# https://leetcode.com/problems/unique-morse-code-words/
# Written 2020-11-22

"""
Transform each word into morse. Add each transformation
into a set, which will remove duplicates. Return the
size of the hash set
"""

class Solution:
    def word_to_morse(self,string):
        #convert each char into its morse representation        
        word = ""
        for char in string:
            #each letter in alphabet in ascii is in order,
            #but offset by 97
            idx = ord(char) - 97
            word += self.char_to_morse[idx]
            
        return word
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        #each letter in alphabet, in order, in morse form
        self.char_to_morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        #adding each tranformation to a set will remove duplicates
        unique_reps = set()
        for word in words:
            unique_reps.add(self.word_to_morse(word))
            
        return len(unique_reps)