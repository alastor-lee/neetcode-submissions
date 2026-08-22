class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        mp = defaultdict(int)
        longest = 0
        for num in uniqueNums:
            length = mp[num - 1] + mp[num + 1] + 1
            mp[num] = length
            mp[num - mp[num - 1]] = length
            mp[num + mp[num + 1]] = length
            longest = length if length > longest else longest
        return longest