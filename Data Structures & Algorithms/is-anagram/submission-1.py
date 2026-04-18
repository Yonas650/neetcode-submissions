class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_hash=defaultdict(int)
        t_hash=defaultdict(int)
        for i in range(len(s)):
            s_hash[s[i]]+=1
            t_hash[t[i]]+=1
        if s_hash!=t_hash: 
            return False
        return True