# https://leetcode.com/problems/find-the-highest-altitude/description/
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]

        for i in range(len(gain)):
            j = altitudes[i] + gain[i]
            altitudes.append(j)

        return max(altitudes)   