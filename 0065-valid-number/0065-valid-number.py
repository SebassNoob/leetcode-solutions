
class Solution:
    def isNumber(self, s: str) -> bool:
        is_finite = False
        try:
            if any(i.isdigit() for i in s):
                is_finite = True
            s = float(s)
            if s in [float("inf"), float("-inf")] and not is_finite:
                return False
            return True
        except:
            return False