class Solution:

    def commonChars(self, words: List[str]) -> List[str]:
        words_size = len(words)
        result = []

        # Initialize common_character_counts with the characters from the first word
        common_character_counts = collections.Counter(words[0])

        for i in range(1, words_size):
            # Count characters in the current word
            current_character_counts = collections.Counter(words[i])

            # Update the common character counts to keep the minimum counts
            for letter in common_character_counts.keys():
                common_character_counts[letter] = min(
                    common_character_counts[letter],
                    current_character_counts[letter],
                )

        # Collect the common characters based on the final counts
        for letter, count in common_character_counts.items():
            for _ in range(count):
                result.append(letter)

        return result