class Solution:
    def minimizedStringLength(self, s: str) -> int:
        setx = set(s)
        return len(setx)