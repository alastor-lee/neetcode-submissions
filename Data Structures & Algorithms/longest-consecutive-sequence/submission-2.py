class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        parents = set()
        mp = defaultdict(int)
        longest = 0
        for num in nums:
            if num in parents: continue
            parents.add(num)
            length = mp[num - 1] + mp[num + 1] + 1
            mp[num] = length
            mp[num - mp[num - 1]] = length
            mp[num + mp[num + 1]] = length
            longest = length if length > longest else longest
        return longest