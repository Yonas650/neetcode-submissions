class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=[0]*26
        maxFreq=0
        distinct=0
        begin=0
        best_len=0
        
        for end in range(len(s)):
            idx=ord(s[end])-ord('A')
            if freq[idx]==0:
                distinct+=1
            freq[idx]+=1
            maxFreq=max(freq)

            while maxFreq+k<end-begin+1:
                left_idx=ord(s[begin])-ord('A')
                freq[left_idx]-=1
                if freq[left_idx]==0:
                    distinct-=1
                begin+=1
            best_len=max(best_len, end-begin+1)
        return best_len