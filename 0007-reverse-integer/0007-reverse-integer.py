class Solution:
    def reverse(self, x: int) -> int:
        res = int(''.join(list(str(x))[::-1])) if (x>0) else int('-'+''.join(list(str(x).replace("-",""))[::-1]))
        return res if -2**31<=res<=2**31-1 else 0