import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        lowercase= list(string.ascii_lowercase)
        
        def generate(word):
            neighbors=[]
            for i in range(len(word)):
                nei=''
                for ch in lowercase:
                    if ch != word[i]:
                        nei=word[:i]+ch+word[i+1:]
                        neighbors.append(nei)
            return neighbors

        queue = deque([(beginWord, 1)])
        visited= set([beginWord])
        
        while queue:

            word, dist= queue.popleft()

            if word==endWord:
                return dist

            neighbors= generate(word)

            for nei in neighbors:
                if nei not in visited and nei in wordList:
                    visited.add(nei)
                    queue.append((nei,dist+1))
                
        return 0

