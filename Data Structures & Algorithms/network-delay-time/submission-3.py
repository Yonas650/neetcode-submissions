class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for ui,vi,ti in times:
            graph[ui].append((vi,ti))
        
        heap = [(0,k)]
        dist = {}

        while heap:
            time, node = heapq.heappop(heap)

            if node in dist:
                continue
            
            dist[node] = time

            for nei, weight in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time+weight, nei))
        if len(dist) != n:
            return -1
        return max(dist.values())