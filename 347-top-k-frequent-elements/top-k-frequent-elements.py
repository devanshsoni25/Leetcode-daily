class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dev=dict()
        pappu=[[] for _ in range(len(nums)+1)]

        for i in range(len(nums)):
            if nums[i] in dev:
                dev[nums[i]]+=1

            else:
                dev[nums[i]]=1


        for key,values in dev.items():
            pappu[values].append(key)

        res=[]
        for i in range(len(pappu)-1,0,-1):
            for key in pappu[i]:
                res.append(key)

                if len(res)==k:
                    return res