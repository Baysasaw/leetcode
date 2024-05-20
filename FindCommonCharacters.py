# https://leetcode.com/problems/find-common-characters/description/
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = [i for i in words[0]]
        

        for i in range(1, len(words)):
            chick = []
            for word in words[i]:
                if word in common:
                    chick.append(word)
                    common.remove(word)
            common = chick
        return common