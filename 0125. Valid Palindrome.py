class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = [t.lower() for t in s if t.isalnum()]

        beg, end = 0, len(string)-1

        while beg<=end:
            if string[beg]!=string[end]:
                return False
            beg += 1
            end -= 1

        return True