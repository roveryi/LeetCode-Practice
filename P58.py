'''
58. Length of Last Word
Easy

650

2396

Add to List

Share
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.split(' ')
        
        while len(s) > 0 and len(s[-1]) == 0:
            
            s.pop()
        
        
        if len(s) == 0:
            return 0
        else:
            return len(s[-1])