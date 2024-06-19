class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # reverse process --> start from sorted then get the deck order
        deck.sort() # start by sorting deck
        n = len(deck)
        res = [0] * n
        q = deque(range(0,n)) # indexes

        for cards in deck:
            i = q.popleft()   # pop index where we insert the popped card (tho not literally poping)
            res[i] = cards

            if q:
                q.append(q.popleft()) # move the next index to the last
        
        return res
