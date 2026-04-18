class TimeMap:

    def __init__(self):
        self.hashmap=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if self.hashmap[key]:
            l,r=0,len(self.hashmap[key])

            while l<r:
                mid=(l+r)//2
                
                if self.hashmap[key][mid][1]<=timestamp:
                    l=mid+1
                else:
                    r=mid
            if l==0:
                return ''
            return self.hashmap[key][l-1][0]
        return ''
