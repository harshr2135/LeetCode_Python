class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[j] == 0 and arr[i] == 0:
                    return True
                elif arr[j] == 0 or arr[i] == 0:
                    continue
                elif arr[i]/arr[j]==2 or arr[j]/arr[i]==2:
                    return True

        return False