class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(1)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix 
            prefix = prefix * nums[i]
        
        suffix = 1

        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * suffix
            suffix = suffix * nums[i]

        return res


        