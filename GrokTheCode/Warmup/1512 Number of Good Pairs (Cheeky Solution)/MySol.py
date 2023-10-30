import math

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for x in nums:
            count[x] += 1

        goodPairs = 0
        for val in count.values():
            goodPairs += math.comb(val,2)
        return goodPairs


//Using Bionomial Coefficent 