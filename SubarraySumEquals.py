# https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        sum_dict = {0: 1}
        for num in nums:
            total += num
            if total - k in sum_dict:
                count += sum_dict[total - k]
            if total in sum_dict:
                sum_dict[total] += 1
            else:
                sum_dict[total] = 1
        return count