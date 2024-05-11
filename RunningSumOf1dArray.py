# https://leetcode.com/problems/running-sum-of-1d-array/
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         for i in range(1, len(nums)):
#             nums[i] += nums[i-1]
#         return nums
    

# the above code can be written as below 


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        numss = []

        for num in nums:
            total += num
            numss.append(total)
        return numss
        