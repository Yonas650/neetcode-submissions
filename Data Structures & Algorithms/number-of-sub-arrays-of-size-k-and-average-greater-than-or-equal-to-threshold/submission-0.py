class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target=k*threshold
        winsum=0
        count=0
        for end in range(len(arr)):
            winsum+=arr[end]

            if end >= k:
                winsum-=arr[end-k]
            if end >=k-1:
                if winsum>=target:
                    count+=1
        return count