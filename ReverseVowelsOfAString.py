# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowes = ['a', 'e', 'i', 'o', 'u','A', 'E', "I", 'O', "U"]
        index = [x for x in s]
        left = 0
        right = len(index) - 1


        while left < right:
            if index[left] in vowes and index[right] in vowes:
                index[left], index[right] = index[right], index[left]
                left += 1
                right -= 1
            else:
                if not index[left] in vowes:
                    left += 1
                if not index[right] in vowes:
                    right -= 1

        return "".join(index)


            
        