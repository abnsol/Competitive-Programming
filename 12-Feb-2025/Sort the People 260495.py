# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        maxx = max(heights) + 1
        n = len(heights)
        cnt = [0] * maxx
        for i in range(n):
            cnt[heights[i]] = names[i]

        sorted_arr = []
        for i in range(maxx - 1,-1,-1):
            if cnt[i] != 0:
                sorted_arr.append(cnt[i])

        return sorted_arr         
