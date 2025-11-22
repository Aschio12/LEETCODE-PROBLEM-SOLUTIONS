class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a1=Counter(arr1)
        a2=set(arr2)
        not_a1=[]
        for n in arr1:
            if n not in a2 and n not in not_a1:
                not_a1.append(n)
        ans=[]
        not_a1.sort()
        for i in arr2:
            ans.extend([i]*a1[i])
        for j in not_a1:
            ans.extend([j]*a1[j])
        return ans
        
            
           
