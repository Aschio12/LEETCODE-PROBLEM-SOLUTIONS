class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a1=Counter(arr1)
        a2=set(arr2)
        not_a1=set()
        for n in arr1:
            if n not in a2 :
                not_a1.add(n)
        ans=[]
        not_a11=sorted(list(not_a1))
        for i in arr2:
            ans.extend([i]*a1[i])
        for j in not_a11:
            ans.extend([j]*a1[j])
        return ans
        
            
           
