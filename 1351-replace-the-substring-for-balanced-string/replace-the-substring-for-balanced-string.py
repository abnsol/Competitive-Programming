class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        cnt = Counter(s)

        if cnt['Q'] == cnt["R"] == cnt["E"] == cnt["W"]:
            return 0

        removeCnt = Counter()
        # find the excess elements
        for key in cnt:
            if cnt[key] > n / 4:
                removeCnt[key] = cnt[key] - n//4
        
        ans = n
        l = 0
        for r in range(n):
            if s[r] in removeCnt:
                removeCnt[s[r]] -= 1
            
            while max(removeCnt.values()) <= 0:
                ans = min(ans, r - l + 1)
                if s[l] in removeCnt:
                    removeCnt[s[l]] += 1
                l += 1
            
        return ans
            

'''
(curCount['W'] >= removeCnt['W'] \
            or curCount['Q'] >= removeCnt['Q'] or \
            curCount['E'] >= removeCnt['E'] or \
            curCount['R'] >= removeCnt["R"])
sliding window
{
    Q : 2
    W : 1
    E : 1
    R : 0
}

R => 1
Q => 1
count the number of unique items and 
QQQWERQQQWWEQWEW
Q : 6 => 2
W : 5 => 1
E : 4 
R : 1
=> 4
QRREERQQQWWEQWEW

w : 8 => 3
E : 4 => 
Q : 5 => 
R : 3 => 
"WWEQERQWQWWRWWERQWEQ"
"WWEQERQRREQRWWERQWEQ"
"RREQERQEQWWRWWERQWEQ"

"WQWRQQQW"
w : 3 => 1
Q : 4 => 2
R : 1 => 
E : 0 => 

'''