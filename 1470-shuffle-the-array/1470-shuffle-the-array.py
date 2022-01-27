class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        l = len(nums)//2
        for i in range(l):
            result.append(nums[i])
            result.append(nums[i+l])
        
        return result