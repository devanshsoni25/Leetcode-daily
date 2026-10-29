class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)

        hash_table = dict()

        for index,values in enumerate(nums):
            if values in hash_table and abs(index-hash_table[values])<=k:
                return True

            hash_table[values] = index
        return False