class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x

        while l<=r:
            mid=(l+r)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                if (mid+1)*(mid+1)<=x:
                    l=mid+1
                else:
                    return mid
            else:
                r=mid-1
