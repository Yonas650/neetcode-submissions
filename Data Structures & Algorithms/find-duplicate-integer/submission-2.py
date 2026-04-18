
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=fast=nums[0]
        #find intersection
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break

        #find the entrance
        slow2=nums[0]
        while slow!=slow2:
            slow=nums[slow]
            slow2=nums[slow2]
        return slow2
        