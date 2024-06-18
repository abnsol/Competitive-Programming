class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def binarySearch(letters, target):
            start, end = 0, len(letters) - 1

            while start <= end:
                mid = (start + end)//2

                if letters[mid] > target:
                    end = mid - 1
                elif letters[mid] < target:
                    start = mid + 1
                else:
                    return mid
            return end

        if target < letters[0] or target >= letters[len(letters) - 1]:
            return letters[0]
        else:
            val = binarySearch(letters,target)
            while val < len(letters) and letters[val] == letters[val + 1]:
                val += 1
            return letters[val + 1]


        