# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            return x == int(str(x)[::-1])