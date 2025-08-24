class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        maxi=salary[0]
        mini=salary[-1]
        salary.remove(maxi)
        salary.remove(mini)
        avg=sum(salary)/len(salary)
        return avg