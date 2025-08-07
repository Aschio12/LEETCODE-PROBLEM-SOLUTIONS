class Solution:
    def canTransform(self, start: str, result: str) -> bool:
     
        s1 = [(i, char) for i, char in enumerate(start) if char != 'X']
        s2 = [(i, char) for i, char in enumerate(result) if char != 'X']
        
        if len(s1) != len(s2):
            return False
            
        for k in range(len(s1)):
            i, char1 = s1[k]
            j, char2 = s2[k]
            if char1 != char2:
                return False
            if char1 == 'L':
                if i < j:
                    return False
            else:
                if i > j:
                    return False
        return True