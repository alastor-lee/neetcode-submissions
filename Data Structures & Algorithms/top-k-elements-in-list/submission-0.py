class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for n in nums:
            countMap[n] = countMap.get(n, 0) + 1
        freqBuckets = [[]] * len(countMap)
        i = 0
        for num, freq in countMap.items():
            freqBuckets[i] = [freq, num]
            i += 1
        freqBuckets.sort()
        print(freqBuckets)
        
        res = []
        while len(res) < k:
            res.append(freqBuckets.pop()[1])
        return res
