class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0
        
        def feasible(k):
            hours = sum(math.ceil(p / k) for p in piles)
            return hours <= h

        l, r = 1, max(piles)
        while l < r:
            mid = (l + (r - 1)) // 2
            if feasible(mid):
                r = mid          # mid подходит — пробуем меньше
            else:
                l = mid + 1       # mid мал — нужно больше
        return l

