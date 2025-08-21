class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for i in grid:
            for j in i[::-1]:
                if j >=0:
                    break
                else:
                    count+=1
        return count