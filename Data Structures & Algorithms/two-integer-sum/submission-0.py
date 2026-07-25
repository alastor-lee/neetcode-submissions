class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        sol = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numMap:
                sol = [i, numMap[diff]] if i < numMap[diff] else [numMap[diff], i]
            else: numMap[nums[i]] = i

        return sol