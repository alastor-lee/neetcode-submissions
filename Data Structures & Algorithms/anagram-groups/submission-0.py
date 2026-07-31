class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countMap = {}
        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord("a")] += 1
            if countMap.get(tuple(count)):
                countMap[tuple(count)].append(str)
            else: 
                countMap[tuple(count)] = [str]
        anaGroups = []
        for k, v in countMap.items():
            anaGroups.append(v)
        return anaGroups