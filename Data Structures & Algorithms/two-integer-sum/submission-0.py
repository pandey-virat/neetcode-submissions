class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,y in enumerate(nums):
            complement = target - y

            if complement in seen:
                return[seen[complement],i]

            seen[y] = i

        

        