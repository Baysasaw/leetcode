# https://leetcode.com/problems/range-sum-query-immutable/description/
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dp = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                self.dp[i] = nums[i]
            else:
                self.dp[i] = self.dp[i-1] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.dp[right]
        return self.dp[right] - self.dp[left-1]
        