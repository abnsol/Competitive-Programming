class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = l = 0
        cnt = {}

        for r in range(len(fruits)):
            cnt[fruits[r]] = cnt.get(fruits[r],0) + 1

            while len(cnt) > 2:
                cnt[fruits[l]] -= 1
                if cnt[fruits[l]] == 0: del cnt[fruits[l]]
                l += 1
            
            res = max(res,r - l + 1)
        
        return res



'''
sw approach

add => elements
check => elements[keys] in the counter only 2
remove => number from left in cnt

counter = {} => elements[keys] in the counter only 2
1, 1 ,2 ,1 ,2, 3, 2 ,2, 2, 2
'''
        