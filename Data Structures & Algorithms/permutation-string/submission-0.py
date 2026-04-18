class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq=[0]*26
        for c in s1:
            freq[ord(c)-ord('a')]+=1
        win=[0]*26
        k=len(s1)

        for end in range(len(s2)):
            idx=ord(s2[end])-ord('a')
            win[idx]+=1
            if end>=k:
                left_idx=ord(s2[end-k])-ord('a')
                win[left_idx]-=1
            if end>=k-1:
                if win==freq:
                    return True
        return False