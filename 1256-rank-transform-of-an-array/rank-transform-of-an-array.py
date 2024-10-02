class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rankArray = sorted(set(arr))
        hashmap = {}
        for idx,num in enumerate(rankArray):
            hashmap[num] = idx + 1
        
        ans = []
        for num in arr:
            ans.append(hashmap[num])

        return ans



'''
save idx in hashmap
sort arr
a = set[10,20,30,40]
hashmap ==> num : idx
new array
then check 
< n square
nlogn

sort the array and convert to set
store the set elements in hashmap {num : idx(rank)}
iterate through the org array then get rank from hashmap and form rank array
'''