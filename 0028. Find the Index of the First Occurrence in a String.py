class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenHaystack = len(haystack)
        lenNeedle = len(needle)
        
        for haystackIdx in range(lenHaystack - lenNeedle + 1):
            needleIdx = 0

            while needleIdx < len(needle) and haystack[haystackIdx + needleIdx] == needle[needleIdx]:
                needleIdx += 1

            if needleIdx == lenNeedle:
                return haystackIdx

        
        return -1