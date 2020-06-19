'''
44. Wildcard Matching
Hard

1876

103

Add to List

Share
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
    
        n = len(s)
        
        dp = [True] + [False] * n
        
        for i in p:
            
            if i != '*':
                
                for j in reversed(range(n)):
                    dp[j+1] = dp[j] and (i == s[j] or i == '?') 
                    
            else:
                
                for j in range(1, n+1):
                    dp[j] = dp[j-1] or dp[j]
                    
            dp[0] = dp[0] and i == '*'
            
        return dp[-1]
                    
