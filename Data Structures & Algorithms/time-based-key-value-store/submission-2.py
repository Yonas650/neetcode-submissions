class TimeMap:

    def __init__(self):
        self.hashmap=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.hashmap[key]:
            return "" 
        
        l,r=0,len(self.hashmap[key])

        while l<r:
            mid=(l+r)//2

            if self.hashmap[key][mid][1]>timestamp:
                r=mid
            else:
                l=mid+1
        if l == 0:
            return ""
        return self.hashmap[key][l-1][0]