class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
       
        if n == 0:
            return

        if n == 1:
            return nums

        k = k%n

        nums.reverse()

        left = 0 
        right = k-1

        while left < right:
            nums[left],nums[right] = nums[right],nums[left]

            left += 1
            right -= 1

        left = k
        right = n-1

        while left < right:
            nums[left],nums[right] = nums[right],nums[left]

            left += 1
            right -= 1

        return nums
