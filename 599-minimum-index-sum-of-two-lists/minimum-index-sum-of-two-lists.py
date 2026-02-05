class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list11={word:i for i,word in enumerate(list1)}
        m=float("inf")
        ans=[]
        for index,val in enumerate(list2):
            if val in list11:
                tot=index+list11[val]
                if tot<m:
                    m=tot
                    ans=[val]
                elif tot==m:
                    ans.append(val)
            
        return ans



