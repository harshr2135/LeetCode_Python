class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elementCount = Counter(nums)

        majElements = []

        for ele, count in elementCount.items():
            if count > len(nums)//3:
                majElements.append(ele)

        return majElements