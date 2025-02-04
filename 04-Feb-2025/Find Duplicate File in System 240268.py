# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = defaultdict(list)
        for i in range(len(paths)):
            flag = 0
            key = ""
            di = paths[i].split()
            filename = ""
            dire = di[0] 
            for j in range(1,len(di)):
                for k in di[j]:
                    if k == "(":
                        flag += 1
                    elif k == ")":
                        flag -= 1
                    else:
                        if flag == 1:
                            key += k
                        else:    
                            filename += k
                files[key].append(dire + "/" + filename)
                key = ""
                filename = ""

        ans = []
        for key in files:
            if len(files[key]) > 1:
                ans.append(files[key])

        return ans
          



            

        