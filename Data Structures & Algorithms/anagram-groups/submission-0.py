class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictOfSortedStrings = {}
        idx = 0
        finalList = []        
        
        for strr in strs:
            sortedStr = "".join(sorted(strr))
            if(dictOfSortedStrings.get(sortedStr) is None):
                dictOfSortedStrings[sortedStr] = idx
                idx+=1
                finalList.append([strr])
            else:
                finalList[dictOfSortedStrings[sortedStr]].append(strr)

        return finalList