class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        d=deque()
        for ch in deck:
            if d:
                d.appendleft(d.pop())
            d.appendleft(ch)
        return list(d)
