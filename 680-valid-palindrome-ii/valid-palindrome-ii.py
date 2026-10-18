class Solution:
    def validPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s)-1

        while low < high:
            if s[low] != s[high]:
                skipL , skipR = s[low+1:high+1] , s[low:high]

                return (skipL == skipL[::-1] or skipR == skipR[::-1])

            low+=1
            high -=1

        return True