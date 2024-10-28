class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # Sort the array in ascending order
        nums.sort()

        # Set to keep track of numbers we've already processed
        processed_numbers = set()

        longest_streak = 0

        # Iterate through each number in the sorted array
        for current in nums:
            # Skip if we've already processed this number
            if current in processed_numbers:
                continue

            streak = current
            streak_length = 1

            # Continue the streak as long as we can find the square of the current number
            while streak * streak <= 10**5:
                if self._binary_search(nums, streak * streak):
                    streak *= streak
                    processed_numbers.add(streak)
                    streak_length += 1
                else:
                    break

            # Update the longest streak if necessary
            longest_streak = max(longest_streak, streak_length)

        # Return -1 if no valid streak found, otherwise return the longest streak
        return longest_streak if longest_streak >= 2 else -1

    # Binary search helper function to efficiently find a value in the sorted array
    def _binary_search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False