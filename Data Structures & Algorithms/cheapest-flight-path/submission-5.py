class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        prices = [INF]*n
        prices[src]= 0

        for _ in range(k+1):
            temp = prices.copy()

            for u,v,cost in flights:

                if prices[u]==INF:
                    continue
                if prices[u]+cost<temp[v]:
                    temp[v]=prices[u]+cost
            prices=temp
            
        return prices[dst] if prices[dst]!=INF else -1