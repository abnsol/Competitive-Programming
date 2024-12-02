class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Initialize the word position counter
        current_word_position = 1
        # Initialize the current index in the sentence
        current_index = 0
        # Get the length of the sentence
        sentence_length = len(sentence)

        # Loop through the sentence
        while current_index < sentence_length:
            # Skip leading spaces
            while (
                current_index < sentence_length
                and sentence[current_index] == " "
            ):
                current_index += 1
                current_word_position += 1

            # Check if the current word starts with searchWord
            matchCount = 0
            while (
                current_index < sentence_length
                and matchCount < len(searchWord)
                and sentence[current_index] == searchWord[matchCount]
            ):
                current_index += 1
                matchCount += 1

            # If the entire searchWord matches, return the current word position
            if matchCount == len(searchWord):
                return current_word_position

            # Move to the end of the current word
            while (
                current_index < sentence_length
                and sentence[current_index] != " "
            ):
                current_index += 1

        # If no match is found, return -1
        return -1