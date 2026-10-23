class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n=len(nums)
        result = []
        nums.sort()

        for i in range(n-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1,n-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
               

                
                p = j+1
                q = n-1

                while p<q:
                    total = nums[i]+nums[j]+nums[p]+nums[q]

                    if total ==target:
                        result.append([nums[i],nums[j],nums[p],nums[q]])
                        p+=1
                        q-=1

                        while p<q and nums[p] == nums[p-1]:
                            p+=1

                        while p<q and q!=n-1 and nums[q] == nums[q+1]:
                            q-=1

                    elif total < target:
                        p+=1

                    else:
                        q-=1
        return result
