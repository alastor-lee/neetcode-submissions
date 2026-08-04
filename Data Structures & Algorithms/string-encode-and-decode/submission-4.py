class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedRes = "";
        for s in strs:
            encodedRes = "".join([encodedRes, str(len(s)), "%", s])
        return encodedRes

    def decode(self, s: str) -> List[str]:
        decodedStrs = [];
        currIndex = 0;
        currStrLen = None;
        while currIndex < len(s):
            if (s[currIndex] == "%") & (currStrLen != None):
                if currStrLen == "0":
                    decodedStrs.append("")
                else:
                    decodedStrs.append(s[currIndex+1:int(currStrLen) + currIndex + 1])
                currIndex += int(currStrLen) + 1
                currStrLen = None
            else:
                if currStrLen:
                    currStrLen = "".join([str(currStrLen), s[currIndex]])
                else:
                    currStrLen = s[currIndex]
                currIndex += 1
        return(decodedStrs)