from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=defaultdict(int)
        
        for i in range(len(nums)):
            hashmap[nums[i]]+=1
        

        sorted_items=sorted(hashmap.items(), key=itemgetter(1),reverse=True)
        res=[]
        for j in range(k):
            res.append(sorted_items[j][0])
        return res