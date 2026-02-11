class Solution:
    def intToRoman(self, num: int) -> str:

        val_symbol={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        vals=list(val_symbol.keys())
        vals.sort(reverse=True)
        ans=""

        for i,ch in enumerate(str(num)):

            if int(ch)==4 or int(ch)==9:
                p=len(str(num))-i-1
                nu=((int(ch)+1)*(10**p))
                ans+=val_symbol[(10**p)]
                ans+=val_symbol[nu]
               

            else:

                base=10**(len(str(num))-i-1)
                current=int(ch)*base
                hold=0
                for nn in vals:
                    while nn<=current and  hold<current:
                        hold+=nn
                        if hold<=current:
                            ans+=val_symbol[nn]
                        else:
                            hold-=nn
                            break
                    
                
        return ans
                    

