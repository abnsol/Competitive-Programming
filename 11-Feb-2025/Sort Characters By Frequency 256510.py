# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        items = list(count.items())

        for i in range(1,len(items)):
            j = i - 1
            key = items[i]
        
            while key[1] > items[j][1] and j >= 0:
                items[j+1] = items[j]
                j -= 1
            items[j+1] = key
    
        return ''.join(key*value for key,value in items)


