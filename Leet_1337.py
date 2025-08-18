class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        final=[]
        res=[]
        for i in range(len(mat)):
            final.append((sum(mat[i]),i))
        final.sort()
        for i in  final[:k]:
            res.append(i[-1])
        return res