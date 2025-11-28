class Solution:
    def firstUniqChar(self, s: str) -> int:
        queue=deque()
        d={}
        for index,val in enumerate(s):
            if val not in d:
                d[val]=1
            else:
                d[val]+=1
            queue.append((val,index))
            while queue and d[queue[0][0]]>1:
                queue.popleft()
        return queue[0][1] if queue else -1
