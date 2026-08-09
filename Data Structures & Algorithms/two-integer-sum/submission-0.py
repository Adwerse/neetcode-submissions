class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            poss = target - x
            if poss in seen:
                return [seen[poss], i]
            seen[x] = i