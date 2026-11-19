class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)

        case_1 = abs(nums[n-1]-nums[2])

        case_2 = abs(nums[n-2]-nums[1])

        case_3 = abs(nums[n-3]-nums[0])

        min_all = min(case_1,case_2,case_3)

        return min_all