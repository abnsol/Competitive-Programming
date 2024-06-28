class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        if len(count) == 1 and list(count.values()) != [1]:
            return True

        n = len(deck)
        for i in range(2,n):
            if n % i == 0:
                cnt = 0
                for key in count:
                    if count[key] != i and count[key] % i != 0:
                        break
                    cnt += count[key]/i
                
                if cnt == n/i:
                    return True
                continue
        return False


        
        
        