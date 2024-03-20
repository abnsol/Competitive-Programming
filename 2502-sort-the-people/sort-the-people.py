class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mymap = {}
        for i in range(len(heights)):
            mymap[heights[i]] = names[i]

        n = len(heights)
    
    
        for i in range(n):
            for j in range(0, n-i-1):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]

        idx = 0
        for key,value in mymap.items():
            names[idx] = mymap[heights[idx]]
            idx += 1
        
        return names


            

        
            