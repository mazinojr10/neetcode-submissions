class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.s = s
        self.t = t
        
        chars1 = list(s)
        chars2 = list(t)

        chars1.sort()
        chars2.sort()

        if chars1 == chars2 :
            return True
        else:
            return False