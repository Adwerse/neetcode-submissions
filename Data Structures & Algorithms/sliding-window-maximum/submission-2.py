from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = 0
        window = deque()

        for r in range(len(nums)):
            while window and window[0] < r - k + 1:
                window.popleft()

            while window and nums[window[-1]] <= nums[r]:
                window.pop()

            window.append(r)

            if r >= k - 1:
                res.append(nums[window[0]])
        
        return res