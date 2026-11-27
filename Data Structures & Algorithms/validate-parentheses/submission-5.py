class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i,x in enumerate(s):
            if len(res) > 0:
                if res[-1] + x in ['()', '{}', '[]']:
                    _ = res.pop()
                    continue
            res.append(x)
        return len(res) == 0

            



        