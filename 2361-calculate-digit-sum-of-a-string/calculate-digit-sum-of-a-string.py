class Solution:
    def digitSum(self, s: str, k: int) -> str:
        s_len = len(s)
        if s_len<=k:
            return s

        new_s = ""
        start = 0

        while start < s_len:

            group = s[start:start+k]

            digit_sum = 0

            for ch in group:
                digit_sum = digit_sum + int(ch)

            new_s = new_s+str((digit_sum))
            start = start+k

        return self.digitSum(new_s,k)
        