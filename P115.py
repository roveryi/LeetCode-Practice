'''
115. Distinct Subsequences
Hard

1285

55

Add to List

Share
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It's guaranteed the answer fits on a 32-bit signed integer.

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
Accepted
137,547
Submissions
360,957
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) == 0:
            return 0
        
        dp = [[0 for j in range(len(s) + 1)] for i in range(len(t) + 1)]
        
        for j in range(len(s) + 1):
            for i in range(len(t) + 1):
                if i == 0:
                    dp[i][j] = 1
                    continue 
                
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                    
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]