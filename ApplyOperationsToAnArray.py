# https://leetcode.com/problems/apply-operations-to-an-array/description/
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for i in range(l - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        nums = [num for num in nums if num != 0]
        nums   =nums +  [0] * (l - len(nums))
        return nums