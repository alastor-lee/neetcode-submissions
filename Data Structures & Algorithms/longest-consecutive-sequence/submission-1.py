class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        consecutives = defaultdict(set)
        longest = 1 if len(nums) > 0 else 0
        #for iNum in range(0, len(uniqueNums)):
        for num in uniqueNums:
            if (num - 1 not in consecutives):
                nextNum = num + 1
                while (nextNum in uniqueNums):
                    consecutives[num].add(nextNum)
                    nextNum += 1
            currLen = len(consecutives[num]) + 1
            # +1 for the parent
            if currLen > longest:
                longest = currLen
        return longest
