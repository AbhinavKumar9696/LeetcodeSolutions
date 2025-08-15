class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        power=0
        const=4
        num=0
        while num<=n:
            num=const**power
            power=power+1
            if num==n:
                return True
        return False