class Solution:
    def __init__(self):
        self.dic={}
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        if n in self.dic:
            return self.dic[n]
        else:
            self.dic[n]=self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]
        
        