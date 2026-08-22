class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        longest = 0
        for num in nums:
            if not mp[num]:
                length = mp[num - 1] + mp[num + 1] + 1
                mp[num] = length
                mp[num - mp[num - 1]] = length
                mp[num + mp[num + 1]] = length
                longest = length if length > longest else longest
        return longest