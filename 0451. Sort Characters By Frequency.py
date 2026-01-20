class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        sortedFreq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        res = ""

        for key, value in sortedFreq:
            res += key*value

        return res