class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def strToHash(self, g: str) -> dict:
            occur = {}
            for char in g:
                if char in occur:
                    occur[char] = occur[char] + 1
                else:
                    occur[char] = 1
            return occur
        # compare the occurrences
        sLetters = strToHash(self, s)
        tLetters = strToHash(self, t)
        if (len(sLetters) != len(tLetters)):
            return False
        for letter in sLetters:
            if (tLetters.get(letter) != sLetters.get(letter)):
                return False
        return True