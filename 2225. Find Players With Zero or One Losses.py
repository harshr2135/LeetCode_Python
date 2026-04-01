class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lossCount = {}

        for winner, loser in matches:
            if winner not in lossCount:
                lossCount[winner] = 0

            lossCount[loser] = lossCount.get(loser,0) + 1

        lossZero = []
        lossOne = []

        for player in lossCount:
            if lossCount[player] == 0:
                lossZero.append(player)

            if lossCount[player] == 1:
                lossOne.append(player)

        return [sorted(lossZero), sorted(lossOne)]