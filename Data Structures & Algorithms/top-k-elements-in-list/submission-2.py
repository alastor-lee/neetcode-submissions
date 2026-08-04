class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for n in nums:
            countMap[n] = countMap.get(n, 0) + 1
        
        # solution: bucket sort
        #freqBuckets = [[]] * (len(nums)+1)
        freqBuckets = [[] for i in range(len(nums) + 1)]
        for num, freq in countMap.items():
            freqBuckets[freq].append(num)

        res = []
        for i in range(len(freqBuckets)-1, 0, -1):
            for n in freqBuckets[i]:
                res.append(n)
                if len(res) == k: return res
        return res
