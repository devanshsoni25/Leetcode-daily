class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        n = len(num_set)

        for i in num_set:
            
            if (i - 1) not in num_set:
                length = 0

                while (i + length) in num_set:
                    length += 1

                longest = max(longest,length)

        return longest

