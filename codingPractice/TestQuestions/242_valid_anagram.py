class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_s = set(s)
        for letter in set_s:
            if t.count(letter) != s.count(letter):
                return False
        return True