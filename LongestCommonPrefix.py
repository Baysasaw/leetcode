# https://leetcode.com/problems/longest-common-prefix/description/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix  = ""
        w = ""
        index = 0
        i = 0
        while  True:
            if len(strs) ==0:
                return prefix
            if index < len(strs[i]):
                if i == 0:
                    w = strs[i][index]
                else:
                    if strs[i][index] != w:
                      return prefix
            else:
                return prefix
            i+=1
            i = i % len(strs)
            if i == 0:
                index += 1
                prefix += w
