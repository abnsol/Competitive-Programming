class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        if num < 0:
            digits = list(str(-num)) # [0,5,6,7]
            return int("-" + "".join(sorted(digits,reverse = True)))
        else:
            digits = sorted(list(str(num))) #[0,1,3]
            for idx,val in enumerate(digits):
                if val != "0":
                    return int(val + "".join(digits[:idx] + digits[idx + 1:])) 


'''
013
103
'''