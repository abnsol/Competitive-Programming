class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        key_len = len(key)
        
        # Find the minimum steps between two indexes of ring
        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)
        
        # HashMap to store the indices of occurrences 
        # of each character in the ring
        character_indicies = collections.defaultdict(list)
        for i, char in enumerate(ring):
            character_indicies[char].append(i)
        
        # Initialize the heap (priority queue) with the starting point
        # Each element of the heap is a tuple of integers representing:
        # totalSteps, ringIndex, keyIndex
        heap = [(0, 0, 0)]
        # tuple in seen: (ringIndex, keyIndex)
        seen = set()
        
        # Spell the keyword using the metal dial
        while heap:
            # Pop the element with the smallest total steps from the heap
            total_steps, ring_index, key_index = heapq.heappop(heap)

            # We have spelled the keyword
            if key_index == key_len:
                break

            # Continue if we have visited this character 
            # from this position in ring before
            if (ring_index, key_index) in seen:
                continue

            # Otherwise, add this pair to the visited list
            seen.add((ring_index, key_index))

            # Add the rest of the occurrences 
            # of this character in ring to the heap
            for next_index in character_indicies[key[key_index]]:
                heapq.heappush(
                        heap, 
                        (total_steps + count_steps(ring_index, next_index),
                        next_index, key_index + 1))

        # Return the total steps and add keyLen to account for 
        # pressing the center button for each character in the keyword
        return total_steps + key_len