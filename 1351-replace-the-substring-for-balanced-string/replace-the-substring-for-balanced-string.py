class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        print(n)
        cnt = Counter(s)
        print(cnt)
        removeCnt = Counter()

        for keys in cnt:
            if cnt[keys] > n/4:
                removeCnt[keys] = cnt[keys] - n//4
        
        if not removeCnt: return 0
        res = n
        l = 0

        for r in range(n):
            if s[r] in removeCnt:
                removeCnt[s[r]] -= 1
            
            while max(removeCnt.values()) <= 0:
                res = min(res,r - l + 1)
                if s[l] in removeCnt:
                    removeCnt[s[l]] += 1
                l += 1
        
        return res


'''
every letter must appear n/4 times
where are those extra letters we dont care about the none extra ones
QQWQQRRRWWQQ
w,r
Q => 3
EEWE
cnt = count s
countExtras = 3
add => subtract count Extras if letter[r] is extra
check if count extras is 0 => update our result which is going to be the min
remove => l elemetn while check is 0
'''