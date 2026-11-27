class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Voc = self.buildVocArr(s1)
        s2Voc = self.buildVocArr(s2[:len(s1)])
        if s2Voc == s1Voc:
            return True

        for i in range(1,len(s2)-len(s1)+1):
            s2Voc = self.editVocArr(s2Voc, s2[i-1], s2[i+len(s1)-1])
            if s2Voc == s1Voc:
                return True
        return False


    def buildVocArr(self, st):
        storeArr = [0]*26
        for c in st:
            idx = ord(c) - ord("a")
            storeArr[idx] += 1
        return storeArr
    
    def editVocArr(self, arr, c1, c2):
        i1 = ord(c1) - ord("a")
        i2 = ord(c2) - ord("a")
        arr[i1] -= 1
        arr[i2] += 1
        return arr









        