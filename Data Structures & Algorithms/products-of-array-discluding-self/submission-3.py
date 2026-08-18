class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        piripirifix = 1
        for i in range(len(nums)):
            res[i] = piripirifix
            piripirifix *= nums[i]
        
        postpostfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postpostfix
            postpostfix *= nums[i]

        return res

