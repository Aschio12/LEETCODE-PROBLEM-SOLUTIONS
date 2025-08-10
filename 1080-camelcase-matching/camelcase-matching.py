class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        results = []
        n = len(pattern)
        for query in queries:
            j = 0
            for char in query:
                if j < n and char == pattern[j]:
                    j += 1
                elif char.isupper():
                    j = -1
                    break
            results.append(j == n)
        return results