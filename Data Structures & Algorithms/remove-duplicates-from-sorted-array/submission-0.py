class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        right_p=1
        k=1
        while right_p<=len(nums)-1:
            if nums[right_p]==nums[right_p-1]:
                right_p+=1
            else:
                nums[k]=nums[right_p]
                k+=1
                right_p+=1
        del nums[k:]
        return k



        
            