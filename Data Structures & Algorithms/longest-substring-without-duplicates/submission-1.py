class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq=[0]*128
        begin=0
        best_len=0
        for end in range(len(s)):
            idx=ord(s[end])
            freq[idx]+=1
            while freq[idx]>1:
                left_idx=ord(s[begin])
                freq[left_idx]-=1
                begin+=1
            best_len=max(best_len, end-begin+1)
        return best_len
        