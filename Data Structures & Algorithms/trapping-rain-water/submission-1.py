class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        maxLeft, maxRight=0,0
        val=0
        while l<r:
            maxLeft=max(maxLeft,height[l])
            maxRight=max(maxRight, height[r])
            if maxLeft<=maxRight:
                if min(maxLeft, maxRight)-height[l]>0:
                    val+=min(maxLeft, maxRight)-height[l]
                l+=1
            else:
                if min(maxLeft, maxRight)-height[r]>0:
                    val+=min(maxLeft, maxRight)-height[r]
                r-=1
        return val