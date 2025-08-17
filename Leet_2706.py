class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        Total = prices[0]+prices[1]

        if Total<=money:
            return money-Total
        else:
            return money