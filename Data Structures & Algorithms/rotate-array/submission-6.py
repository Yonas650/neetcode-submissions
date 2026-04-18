class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        def inverse(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]

                l,r=l+1, r-1
        inverse(0,len(nums)-1)
        inverse(0,k-1)
        inverse(k,len(nums)-1)


            