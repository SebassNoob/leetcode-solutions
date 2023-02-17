class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] !=9:
            digits[-1] += 1
        else:
            digits[-1] =0
            n= -2
            try:
                while digits[n] == 9 :
                    digits[n] = 0
                    if (-n) != len(digits):
                        n -=1
                    else: 
                        
                        raise IndexError
                digits[n] += 1
            except IndexError:
                digits.insert(0,1)
        return digits