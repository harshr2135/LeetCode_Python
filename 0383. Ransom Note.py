class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26
        
        for charMag in magazine:
            count[ord(charMag) - 97] += 1

        for charNote in ransomNote:
            count[ord(charNote) - 97] -= 1
            if count[ord(charNote) - 97] < 0:
                return False


        return True