class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        currCapacity = capacity
        for i in range(len(plants)):
            while currCapacity < plants[i]:
                currCapacity = capacity
                steps += 2 * (i)
            
            currCapacity -= plants[i]
            steps += 1             
        
        return steps

