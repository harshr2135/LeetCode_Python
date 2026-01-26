class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        arr.sort()

        min = inf

        for idx in range(len(arr)-1):
            diff = arr[idx + 1] - arr[idx]
            if diff < min:
                min = diff
                res = []
            
            if diff == min:
                res.append([arr[idx], arr[idx+1]])

        return res