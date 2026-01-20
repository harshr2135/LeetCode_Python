class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        key = "".join(sorted(p))

        idxArray = []

        for idx in range(len(s)-len(p)+1):
            subString = "".join(sorted(s[idx:idx+len(p)]))
            if subString == key:
                idxArray.append(idx)

        return idxArray