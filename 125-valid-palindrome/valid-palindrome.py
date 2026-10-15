class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
       
        for ch in s:
            if ch.isalnum():
                result += ch
        
        result=result.lower()

        low=0
        high=len(result)-1

        while low < high:
            if result[low] != result[high]:
                return False
            low+=1
            high-=1

        return True    