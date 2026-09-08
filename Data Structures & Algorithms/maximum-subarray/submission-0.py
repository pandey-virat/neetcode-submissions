class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]

        curr_num = 0
        for num in nums:
            if curr_num < 0:
                curr_num = 0
            
            curr_num += num

            max_sub = max(max_sub, curr_num)

        return max_sub
        