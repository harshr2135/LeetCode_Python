class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1

        pos = -1

        while left <= right:
            mid = (left+right)//2

            if letters[mid] > target:
                pos = mid
                right = mid -1

            else:
                left = mid + 1

        return letters[pos] if pos != -1 else letters[0] 