class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap=[-num for num in nums]

        heapq.heapify(max_heap)

        stop=1
        while stop<=k:
            res=heapq.heappop(max_heap)
            if stop==k:
                return -res
            stop+=1