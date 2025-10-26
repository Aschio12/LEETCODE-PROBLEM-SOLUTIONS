class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job=sorted(zip(difficulty,profit))
        i,ans,best=0,0,0
        worker.sort()
        for c in worker:
            while i<len(job) and c>=job[i][0]:
                best=max(best,job[i][1])
                i+=1
            ans+=best
        return ans