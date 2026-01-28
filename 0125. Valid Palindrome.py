class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""

        for ch in s:
            if ch.isalnum():
                string += ch

        string = string.lower()

        return string == string[::-1]