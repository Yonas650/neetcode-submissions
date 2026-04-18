class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight, minVal=[],[],[]
        
        for i in range(len(height)):
            if i==0:
                max_left=0
            else:
                max_left=max(max_left,height[i-1])
            
            maxLeft.append(max_left)
        for i in range(len(height)-1,-1, -1):
            if i ==len(height)-1:
                max_right=0
            else:
                max_right=max(max_right, height[i+1])
            maxRight.append(max_right)
        maxRight.reverse()

        minVal=[min(l,r) for l,r in zip(maxLeft, maxRight)]
        res=0
        for i in range(len(minVal)):
            val=minVal[i]-height[i]
            if val >0:
                res+=val
        return res