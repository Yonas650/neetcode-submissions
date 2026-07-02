class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        lowercase = [chr(i) for i in range(ord('a'), ord('z')+1)]
        wordSet = set(wordList)

        def generate(word):
            neighbors = []
            for i in range(len(word)):
                nei=''
                for ch in lowercase:
                    if ch!=word[i]:
                        nei=word[:i]+ch+word[i+1:]
                        neighbors.append(nei)
            return neighbors
        
        queue=deque([(beginWord,1)])
        visited=set([beginWord])
        while queue:
            node, dist = queue.popleft()

            if node == endWord:
                return dist
            
            neighbors = generate(node)

            for nei in neighbors:
                if nei in wordSet and nei not in visited:
                    visited.add(nei)
                    queue.append((nei, dist+1))
        
        return 0
