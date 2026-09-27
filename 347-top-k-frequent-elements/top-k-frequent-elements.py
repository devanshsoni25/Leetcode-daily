class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dev=dict()
        pappu=[]

        for i in range(len(nums)):
            if nums[i] in dev:
                dev[nums[i]]+=1

            else:
                dev[nums[i]]=1


        result=dict(sorted(dev.items(),key=lambda x:x[1],reverse=True))
        
        for key,values in result.items():
            if len(pappu)<k:
                pappu.append(key)

        return pappu
