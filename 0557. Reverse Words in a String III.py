class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split()
        revWordList = [word[::-1] for word in wordList]
        return " ".join(revWordList)