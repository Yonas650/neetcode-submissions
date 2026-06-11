class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count= Counter(tasks)
        heap=[-count for count in count.values()]
        heapq.heapify(heap)
        cooldown=deque() #(timetobeReady, count)
        time=0

        while heap or cooldown:
            time+=1
            #if a task finished cooling down put it to heap
            if cooldown and cooldown[0][0]<=time:
                ready_time, count= cooldown.popleft()
                heapq.heappush(heap, count)
            
            #if there is task available run the most frequent one
            if heap:
                count=heapq.heappop(heap)
                count+=1 #since count is negative

                #if there are more copies of the same task put it back to cool down
                if count<0:
                    cooldown.append((time+n+1, count))
        return time