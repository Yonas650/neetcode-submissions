class Twitter:

    def __init__(self):
        
        self.time=0
        self.tweets=defaultdict(list) #userId -> [(time, tweetId)]
        self.following=defaultdict(set)#userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        result=[]

        users=set(self.following[userId])
        users.add(userId)

        for uid in users:
            if self.tweets[uid]:
                idx=len(self.tweets[uid])-1

                time, tweetId=self.tweets[uid][idx]

                heapq.heappush(heap, (-time, tweetId, idx, uid))
        while heap and len(result)<10:
            neg_time, tweetId, idx, uid=heapq.heappop(heap)
            result.append(tweetId)

            prev_idx=idx-1

            if prev_idx>=0:
                time, prev_tweetId=self.tweets[uid][prev_idx]

                heapq.heappush(heap, (-time, prev_tweetId, prev_idx, uid))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
         self.following[followerId].discard(followeeId)
