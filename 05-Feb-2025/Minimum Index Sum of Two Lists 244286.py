# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        count_list1 = {val : idx for idx,val in enumerate(list1)}
        count_list2 = {val : idx for idx,val in enumerate(list2)}
        count_common = {}
        for key in count_list1:
            if key in count_list2:
                count_common[key] = count_list1[key] + count_list2[key]
        
        new = sorted(count_common.items(),key = lambda a:a[1])
        min_idx = new[0][1]
        ans = []
        for key,idx in new:
            if idx == min_idx:
                ans.append(key)
        
        return ans
