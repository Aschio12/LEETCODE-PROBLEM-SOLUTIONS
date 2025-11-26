class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count,ticketIndex=0,deque()

        for index,ticket in enumerate(tickets):
            ticketIndex.append([ticket,index])
        while True:
            ticketIndex[0][0]-=1
            count+=1
            if ticketIndex[0][1]==k and ticketIndex[0][0]==0:
                return count
            elif ticketIndex[0][0]!=0:
                t=ticketIndex.popleft()
                ticketIndex.append(t)
            else:
                ticketIndex.popleft()
            
                

