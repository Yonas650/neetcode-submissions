class Solution:
    def __init__(self):
        pass
    def check(self,piles, m):
        summ=0
        for i in piles:
            summ=summ+ math.ceil(i/m)
        return summ
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l<=r:
            m=(l+r)//2
            if self.check(piles,m)<=h:
                r=m-1
            else:
                l=m+1
        return l