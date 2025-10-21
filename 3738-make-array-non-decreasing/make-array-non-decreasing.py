class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        prev,stack=0,[]
        for num in nums:
            if num>=prev:
                stack.append(num)
                prev=num
        return len(stack)
        