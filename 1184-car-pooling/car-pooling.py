class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        minheap=[]
        current_passengers=0
        for s in trips:
            numpass,start,end=s
            current_passengers+=numpass
            while minheap and minheap[0][0]<=start:
                current_passengers-=heapq.heappop(minheap)[1]
                

            if current_passengers>capacity:
                return False
            heapq.heappush(minheap,[end,numpass])
        return True