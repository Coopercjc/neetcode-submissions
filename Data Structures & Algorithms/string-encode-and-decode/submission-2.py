class Solution:

    def encode(self, strs: List[str]) -> str:
        count=0
        finalstr = ""

        for s in strs:
            finalstr += f"{len(s)}#{s}"
        return finalstr
    def decode(self, s: str) -> List[str]:
        finalList = []
        
        while len(s) != 0:
            index = s.find("#")
            length = int(s[:index])
            newword= s[index+1:index+1+length]
            finalList.append(newword)
            s = s[index+1+length:]
        return finalList

