from math import inf
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq=[0]*128 #how many of each char we need
        for c in t:
            freq[ord(c)]+=1
        counter=len(t) #number of chars missing for the window to be valid
        best_len=inf
        best_start=0
        begin=0

        for end in range(len(s)):
            idx=ord(s[end])
            if freq[idx]>0:
                counter-=1
            freq[idx]-=1

            while counter==0:
                window_len=end-begin+1
                if window_len<best_len:
                    best_len= window_len
                    best_start=begin
                left_idx=ord(s[begin])
                freq[left_idx]+=1
                if freq[left_idx]>0:
                    counter+=1
                begin+=1
        if best_len==inf:
            return ''
        return s[best_start:best_start+best_len]
