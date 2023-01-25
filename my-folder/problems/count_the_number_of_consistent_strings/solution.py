class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed, count = set(allowed), 0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    count += 1
                    break
        return len(words)-count
