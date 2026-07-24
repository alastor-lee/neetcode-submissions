class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        sMap = {}
        tMap = {}

        for i in range(0, len(s)):
            sChar = s[i]
            tChar = t[i]
            if sChar in sMap:
                sMap[sChar] = sMap[sChar] + 1
            else:
                sMap[sChar] = 1

            if tChar in tMap:
                tMap[tChar] = tMap[tChar] + 1
            else:
                tMap[tChar] = 1
        
        for letter in sMap:
            if (sMap.get(letter) != tMap.get(letter)):
                return False

        return True