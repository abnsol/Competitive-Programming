class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
    
        def canship(max_capacity):
            current_weight, day_count = 0, 1  
            for weight in weights:
                current_weight += weight 
                if current_weight > max_capacity:
                    day_count += 1
                    current_weight = weight
            
            return day_count <= days

        left, right = max(weights), sum(weights)
      
        min_capacity_needed = left + bisect_left(range(left, right), True, key=canship)
      
        return min_capacity_needed