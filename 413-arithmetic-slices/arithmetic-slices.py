class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        else:
            count,start=0,0
            while start<len(nums)-2:
                left,right=start,start+1
                current=nums[right]-nums[start]
                left+=1
                right+=1
                while right<len(nums):
                    if nums[right]-nums[left]==current:
                        if right-start+1>=3:
                            count+=1
                        left+=1
                        right+=1
                    else:
                        break
                start+=1
            return count
                

            
            
            