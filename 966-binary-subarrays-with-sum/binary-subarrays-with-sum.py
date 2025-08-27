class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l, ans, current = 0, 0, 0
        for r in range(len(nums)):
            current += nums[r]
            if goal == 0:
                if nums[r] == 1:
                    l = r + 1
                else:
                    ans += (r - l + 1)
            else:
                while current > goal and l <= r:
                    current -= nums[l]
                    l += 1
                if current == goal:
                    countZeros = 0
                    t = l
                    while t <= r and nums[t] == 0:
                        countZeros += 1
                        t += 1
                    ans += countZeros + 1
        return ans