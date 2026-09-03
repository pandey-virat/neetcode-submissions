class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)

        if not nums:
            return 0

        longest_seq = 1
        count = 1

        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]

            if diff == 1:
                count += 1

                if count > longest_seq:
                    longest_seq = count

            elif diff == 0:
                pass

            else:
                count = 1

        return longest_seq