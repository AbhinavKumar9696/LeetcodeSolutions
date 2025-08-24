class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        visited = []
        total = 0
        n = len(mat)
        for i in range(n):
            if (i,i) not in visited:
                total += mat[i][i]
                visited.append((i,i))
            if (i, n-1-i) not in visited:
                total += mat[i][n-1-i]
                visited.append((i, n-1-i))
        return total