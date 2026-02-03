class Solution:
    def compress(self, chars: List[str]) -> int:
        count=0
        read,write,left=0,0,0
        while read<len(chars):
            while read<len(chars) and chars[read]==chars[left]:
                read+=1
            chars[write]=chars[left]
            write+=1
            if read-left>1: 
                for char in (str(read-left)):
                    chars[write]=char
                    write+=1
            left=read
        return write

        
       
            
        