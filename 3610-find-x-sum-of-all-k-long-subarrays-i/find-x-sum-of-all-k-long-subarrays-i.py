class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        result = []
        for i in range(0, n - k + 1):
            subarray = nums[i:i+k]
            freq = {}
            for num in subarray:
                freq[num] = freq.get(num, 0) + 1
            items = []
            for num, count in freq.items():
                items.append((count, num))
            items.sort(key=lambda item: (-item[0], -item[1]))
            top_nums = set()
            for j in range(min(x, len(items))):
                top_nums.add(items[j][1])
            total = 0
            for num in subarray:
                if num in top_nums:
                    total += num
            result.append(total)
        return result