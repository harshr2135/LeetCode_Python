class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        arr = list(str(n))
        marker = len(arr)

        for idx in range(len(arr)-1 , 0, -1):
            if arr[idx-1] > arr[idx]:
                arr[idx-1] = str(int(arr[idx-1]) - 1)
                marker = idx

        for idx in range(marker, len(arr)):
            arr[idx] = '9'

        return int(''.join(arr))