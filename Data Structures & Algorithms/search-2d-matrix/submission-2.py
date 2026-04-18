class Solution:
    def binarySearch(self, nums, target):
            l,r=0,len(nums)-1

            while l<=r:
                mid=(l+r)//2

                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    return True
            return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0, len(matrix)-1

        while l<=r:
            mid=(l+r)//2
            if target<matrix[mid][0]:
                r=mid-1
            elif target>matrix[mid][-1]:
                l=mid+1
            else:
                return self.binarySearch(matrix[mid],target)
        return False
        