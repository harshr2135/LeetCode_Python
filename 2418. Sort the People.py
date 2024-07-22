class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = dict(zip(heights, names))
        keys = list(dic.keys())
        keys.sort(reverse=True)
        values = []
        return [(dic[k]) for k in keys]