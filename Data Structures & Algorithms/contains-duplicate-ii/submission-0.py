class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set()

        for end in range(len(nums)):
            if nums[end] in window:
                return True
            window.add(nums[end])
            if end>=k:
                window.remove((nums[end-k]))

        return False