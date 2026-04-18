import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi= 1, max(piles)

        def ok(k):
            total=0
            for pile in piles:
                total+=math.ceil(pile/k)
            return total<=h
        while lo<hi:
            mid=(lo+hi)//2
            if ok(mid):
                hi=mid
            else:
                lo=mid+1
        return lo