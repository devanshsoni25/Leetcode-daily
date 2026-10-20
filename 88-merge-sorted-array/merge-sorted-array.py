class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m+n-1

        j = len(nums2) - 1

        while i >= m or j>0:
            nums1[i] = nums2[j]
            i-=1
            j-=1

        nums1.sort()
