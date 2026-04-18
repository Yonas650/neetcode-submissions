class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        nums1=nums[:len(nums)-k]
        nums2=nums[len(nums)-k:]
        nums[:]=nums2+nums1
         