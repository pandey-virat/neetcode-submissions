class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i,y in enumerate(nums):
            if y == target:
                return i
        return -1

        