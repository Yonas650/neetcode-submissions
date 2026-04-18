import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        m,n=len(A),len(B)
        if m>n:
            A,B=B,A
            m,n=n,m
        half=(m+n+1)//2
        lo,hi=max(0,half-n), min(m,half)

        while lo<=hi:
            i=(lo+hi)//2
            j=half-i
            LA=A[i-1] if i>0 else float(-math.inf)
            RA=A[i] if i<m else float(math.inf)

            LB=B[j-1] if j>0 else float(-math.inf)
            RB=B[j] if j<n else float(math.inf)

            if LA <=RB and LB<=RA:
                left_max=max(LA,LB)
                if (m+n)%2==1:
                    return left_max
                right_min=min(RA,RB)
                return (left_max+right_min)/2
            if LA>RB:
                hi=i-1
            else:
                lo=i+1
        return 0.0
            