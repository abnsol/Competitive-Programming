class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        
        minheap = []
        for key, val in freq.items():
            heapq.heappush(minheap, (-val, key))
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(minheap)[1])
        
        return ans
