class Solution:
    def numberOfSteps(self, num: int,step=0) -> int:
        if num==0:
            return step
        if num%2==0:
            return self.numberOfSteps(num//2,step+1)
        else:
            return self.numberOfSteps(num-1,step+1)
        