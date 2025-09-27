class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s,p,prefix,suffix=0,0,[],[]
        for i in range(len(nums)):
            p+=nums[i]
            prefix.append(p-nums[i])
        for i in range(len(nums)-1,-1,-1):
            s+=nums[i]
            suffix.append(s-nums[i])
        suffix=suffix[::-1]
        for i in range(len(suffix)):
            if prefix[i]==suffix[i]:
                return i
        return -1
        

        