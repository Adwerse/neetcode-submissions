class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {} # keys are number + freq

        for i in range(len(nums)):
            seen[nums[i]] = seen.get(nums[i], 0) + 1
        
        return max(seen, key=seen.get)
