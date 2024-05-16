# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/submissions/1259659008/
class Solution:    
    def freqAlphabets(self, s: str) -> str:
        alphabet_dict = {str(i - 96): chr(i) for i in range(ord('a'), ord('z') + 1)}
        out = ""
        start = 0
        end = 1

        while end < len(s):
            if s[end] == "#" and end - start == 2:
                out += alphabet_dict[s[start:end]]

                start = end + 1
                end += 1
            elif end - start> 2:
                out += alphabet_dict[s[start]]
                start += 1
                if end == "#":
                    end += 1
            else:
                end += 1
        if end == len(s) and start != len(s):
            for i in range(start,end):
                    out += alphabet_dict[s[i]]
        return out         
                
           








# class Solution:
#     def freqAlphabets(self, s: str) -> str:
#         result = ""
#         i = 0
#         while i < len(s):
#             if i + 2 < len(s) and s[i + 2] == "#":
#                 result += chr(int(s[i:i + 2]) + 96)
#                 i += 3
#             else:
#                 result += chr(int(s[i]) + 96)
#                 i += 1
#         return result