class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=[0]*26
        begin=0
        max_freq=0
        best_len=0

        for end in range(len(s)):
            idx=ord(s[end])-ord('A')
            freq[idx]+=1
            max_freq=max(max_freq, freq[idx])

            while (end-begin+1)-max_freq>k:
                left_idx=ord(s[begin])-ord('A')
                freq[left_idx]-=1
                begin+=1
            best_len= max(best_len, end-begin+1)

        return best_len
