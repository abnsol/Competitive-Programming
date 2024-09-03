class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Convert each character to its numerical value and build a string
        numeric_string = ""
        for ch in s:
            numeric_string += str(ord(ch) - ord("a") + 1)

        # Apply digit sum transformations k times
        while k > 0:
            digit_sum = 0
            for digit in numeric_string:
                digit_sum += int(digit)
            numeric_string = str(digit_sum)
            k -= 1

        # Convert the final string to integer and return
        return int(numeric_string)