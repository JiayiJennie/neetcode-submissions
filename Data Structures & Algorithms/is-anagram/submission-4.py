class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.s = s
        self.t = t
        self.smap = {}  # char : times
        self.tmap = {}
        if len(s) == len(t):
            l = len(s)
            self.buildmap(l)
            return self.checkanagrams()
        else:
            return False
    
    def buildmap(self, l):
        for i in range(l):
            schar = self.s[i]
            tchar = self.t[i]

            if schar in self.smap:
                self.smap[schar] += 1
            else:
                self.smap[schar] = 1

            if tchar in self.tmap:
                self.tmap[tchar] += 1
            else:
                self.tmap[tchar] = 1

    def checkanagrams(self):
        for k in self.smap:
            if k in self.tmap:
                if self.smap[k] == self.tmap[k]:
                    continue
                else:
                    return False
            else:
                return False
        return True

        