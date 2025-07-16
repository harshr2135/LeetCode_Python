class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()
        vowels = "aeiou"
        if (len(word)>=3 and word.isalnum() and any(c in vowels for c in word if c.isalpha()) and any(c not in vowels for c in word if c.isalpha())):
                return True
        return False