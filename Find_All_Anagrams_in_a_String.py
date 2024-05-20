# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     result = []
    #     target_counts = collections.Counter(p)
    #     window_counts = collections.Counter(s[:len(p) - 1])

    #     for i in range(len(p) - 1, len(s)):
    #         curr_char = s[i]
    #         window_counts[curr_char] += 1
    #         if window_counts == target_counts:
    #             result.append(i - len(p) + 1)

    #         window_counts[s[i - len(p) + 1]] -= 1
    #         if window_counts[s[i - len(p) + 1]] == 0:
    #             del window_counts[s[i - len(p) + 1]]

    #     return result




    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        counts = 0
        target = collections.Counter(p)
        for i in range(len(s)-len(p) + 1):
            if(collections.Counter(s[i : i + len(p)]) == target):
                result.append(i)
        return result
