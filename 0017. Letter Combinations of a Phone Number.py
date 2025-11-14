class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        res = ['']

        for num in digits:
            temp = []
            for s in res:
                for ch in letters[int(num)]:
                    temp.append(s+ch)

            res = temp

        return res