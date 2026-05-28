import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]

        for point in points:
            distance=((point[0]**2 + point[1]**2)**0.5)
        
            heapq.heappush(heap,(-distance,point))

            if len(heap)>k:
                heapq.heappop(heap)
        for i in range(len(heap)):
            heap[i]=heap[i][1]
        return heap