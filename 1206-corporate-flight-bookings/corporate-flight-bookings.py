class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], m: int) -> List[int]:
        n=200000
        mark=[0]*n
        minn,maxx=n,1
        for first,last,seats in (bookings):
            mark[first]+=seats
            mark[last+1]-=seats
            maxx=max(maxx,last)
            minn=min(minn,first)
        prefix=[0]*n
        prefix[0]=mark[0]
        for i in range(minn,maxx+1):
            prefix[i]=mark[i]+prefix[i-1]
        ans=[]
        for i in range(1,m+1):
            ans.append(prefix[i])
        return ans
