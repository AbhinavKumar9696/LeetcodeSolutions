class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zero_count = total = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                zero_count = 0
            total+= zero_count
            
        return total