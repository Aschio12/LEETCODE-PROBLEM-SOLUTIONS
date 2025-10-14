class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue=deque()
        for i in range(len(tickets)):
            queue.append([tickets[i],i])
        count=0
        while True:
            if queue[0][0]>0:
                queue[0][0]-=1
                count+=1
            if queue[0][0]==0 and queue[0][1]==k:
                return count
            else:
                queue.append(queue[0])
                queue.popleft()
            

