class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        mark=[0]*200001
        for first,last,seats in (bookings):
            mark[first]+=seats
            mark[last+1]-=seats
        prefix=[0]*200001
        prefix[0]=mark[0]
        for i in range(1,len(prefix)):
            prefix[i]=mark[i]+prefix[i-1]
        ans=[]
        for i in range(1,n+1):
            ans.append(prefix[i])
        return ans
