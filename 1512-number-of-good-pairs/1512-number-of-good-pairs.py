class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        result = 0
        
        for num in counter.values():
            n = num-1
            result += n*(n+1)//2
        return result