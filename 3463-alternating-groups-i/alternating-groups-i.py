class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count=0
        for l in range(len(colors)):
            end=(l+2)%len(colors)
            if end>l:
                current=colors[l:end+1]
            else:
                current=colors[l:]+colors[:end+1]
            if current[1]!=current[0] and current[1]!=current[-1]:
                count+=1
        return count

