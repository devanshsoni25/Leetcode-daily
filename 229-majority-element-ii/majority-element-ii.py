class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n=len(nums)
        l=[]
        major = {}

        for num in nums:
            if num not in major:
                major[num]=1
            else:
                major[num]+=1

        for key,values in major.items():
            if values>n//3:
                l.append(key)

        return l
