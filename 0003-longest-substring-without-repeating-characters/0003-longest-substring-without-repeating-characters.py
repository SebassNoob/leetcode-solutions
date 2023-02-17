class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        test = ""
        maxLength = 0
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        for c in list(s):
            current = "".join(c)
            
            # If string already contains the character
            # Then substring after repeating character
            if (current in test):
                test = test[test.index(current) + 1:]
            test = test + "".join(c)
            maxLength = max(len(test), maxLength)
        return maxLength

            
