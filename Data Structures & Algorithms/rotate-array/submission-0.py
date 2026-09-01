class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        lst = nums[-k:]
        nums[-k:] = []
        nums[:] = lst + nums

        return nums
        