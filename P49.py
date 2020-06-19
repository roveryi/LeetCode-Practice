'''
49. Group Anagrams
Medium

3402

178

Add to List

Share
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dicts = {}
        for i in strs:
            i_t = tuple(sorted(tuple([k for k in i])))
            if i_t in dicts.keys():
                dicts[i_t].append(i)
                
            else:
                dicts[i_t] = [i]
                
        ans = []
        for i, j in dicts.items():
            ans.append(j)
        
        return ans 
            
        