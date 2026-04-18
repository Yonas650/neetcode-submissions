
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       hashmap=defaultdict(int)
       for num in nums:
        if hashmap[num]>=1:
            return num
        hashmap[num]+=1
        