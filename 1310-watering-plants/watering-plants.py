class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        left = steps = 0
        currCapacity = capacity
        while left < len(plants):
            if currCapacity >= plants[left]:
                currCapacity -= plants[left]
                steps += 1
                left += 1
            else:
                currCapacity = capacity
                steps += 2 * (left)
        
        return steps

