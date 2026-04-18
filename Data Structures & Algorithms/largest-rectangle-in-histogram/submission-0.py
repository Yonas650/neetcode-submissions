class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        stack=[]
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                max_area=max((i-index)*height, max_area)
                start=index
            stack.append((start,h))
        

        for i,h in stack:
            max_area=max((len(heights)-i)*h, max_area)

        return max_area
