class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def feasible(k): # Where k is bananas/hour
            hours = sum(math.ceil(p / k) for p in piles) # For each pile in array piles     looking for it's hours in which we can eat them
            return hours < h #Checking if we ulozhilis in our max h

        l, r = 1, max(piles)
        while l < r:
            mid = (l + (r - 1)) // 2

            if feasible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l



