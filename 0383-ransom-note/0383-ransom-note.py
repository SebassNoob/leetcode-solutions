class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        try:
            a= list(magazine)
            for i in ransomNote:
                a.remove(i)
            return True
        except ValueError:
            return False
                