class Solution:
    def findMin(self, nums: List[int]) -> int:
        last=nums[-1]
        l,r=0, len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]<=last:
                r=mid
            else:
                l=mid+1
        return nums[l]