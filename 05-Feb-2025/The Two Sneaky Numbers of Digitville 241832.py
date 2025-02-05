# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        digit_ville = Counter(nums)
        return [key for key in digit_ville if digit_ville[key] > 1]              