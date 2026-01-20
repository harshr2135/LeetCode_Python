class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stoneFreq = {}

        for stone in stones:
            stoneFreq[stone] = stoneFreq.get(stone, 0) + 1

        count = 0
        for jewel in jewels:
            if jewel in stoneFreq.keys():
                count += stoneFreq[jewel]

        return count