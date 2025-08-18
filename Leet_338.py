class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            val=bin(i)[2:]
            count=val.count("1")
            ans.append(count)
        return ans