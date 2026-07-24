class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = set()
        for i in nums:
            print(i)
            if i in track:
                return True
            else:
                track.add(i)
        return False
        