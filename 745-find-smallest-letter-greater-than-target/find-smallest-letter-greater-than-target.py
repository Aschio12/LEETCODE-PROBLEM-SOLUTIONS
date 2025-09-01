class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lett=list(set(letters))
        lett.sort()
        ans=""
        for i in lett:
            if ord(i)>ord(target):
                ans=i
                break
        return ans if ans else letters[0]