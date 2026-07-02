class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        def dfs(i):

            visited.add(i)

            for nei in graph[i]:
                if nei not in visited:
                    dfs(nei)
        count=0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count+=1
        return count
       