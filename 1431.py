class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        kidsThatCanHaveMaxCandies = []
        for candy in candies:
            kidsThatCanHaveMaxCandies.append(candy + extraCandies >= maxCandy)
        return kidsThatCanHaveMaxCandies
