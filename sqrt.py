# https://leetcode.com/problems/sqrtx/description/

class solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        # binary search
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right