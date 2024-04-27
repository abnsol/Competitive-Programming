class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        cnt = {}
        ans = 0

        for w, h in rectangles:
            ratio = w/h
            if ratio not in cnt:
                cnt[ratio] = cnt.get(ratio,0)
            else:
                cnt[ratio] += 1
                ans += cnt[ratio]
        
        return ans
            
        