class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total = 0
        n = len(timeSeries)
        for i in range(n - 1):
            total += min(duration, timeSeries[i+1] - timeSeries[i])
        total += duration
        return total