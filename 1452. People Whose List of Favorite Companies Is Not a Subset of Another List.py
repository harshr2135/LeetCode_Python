class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        unique = []

        company = [set(comp) for comp in favoriteCompanies]

        for i in range(len(favoriteCompanies)):
            found = False
            for j in range(len(favoriteCompanies)):
                if i == j:
                    continue
                if company[i].issubset(company[j]):
                    found = True
                    break
            if not found:
                unique.append(i)
        
        return unique