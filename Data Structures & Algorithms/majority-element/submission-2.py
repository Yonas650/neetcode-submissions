class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        res=0

        for i in range(len(nums)):
            
                if nums[i]==res:
                    count+=1
                elif nums[i]!=res and count!=0:
                    count-=1
                elif nums[i]!=res and count==0:
                    res=nums[i]
                    count+1
        return res
