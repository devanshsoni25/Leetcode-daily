class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        count=1
        max_count=1
        i=1

        while i<len(nums):

            if nums[i] == nums[i-1]+1:
                count+=1

            elif nums[i] == nums[i-1]:
                pass

            else:
                count=1

            max_count=max(count,max_count)
            i+=1

        return max_count