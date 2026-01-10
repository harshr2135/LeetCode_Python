class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        
        idx = 0
        while idx+1 < len(arr) and arr[idx] < arr[idx+1]:
            idx += 1

        if idx == 0 or idx == len(arr)-1:
            return False

        while idx+1<len(arr) and arr[idx]>arr[idx+1]:
            idx += 1

        return idx == len(arr)-1
