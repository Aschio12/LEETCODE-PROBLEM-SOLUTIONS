class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = []
        p = 0
        for num in nums:
            p += num
            prefix.append(p)
        
        def binary_search(q):
            left, right = 0, len(prefix) - 1
            while left <= right:
                mid = (left + right) // 2
                if prefix[mid] <= q:
                    left = mid + 1
                else:
                    right = mid - 1
            return left  # This is the count of elements that satisfy the condition
        
        ans = []
        for q in queries:
            count = binary_search(q)
            ans.append(count)
        return ans