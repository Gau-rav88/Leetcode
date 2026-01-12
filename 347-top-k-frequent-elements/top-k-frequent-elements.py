class Solution(object):
    def topKFrequent(self, nums, k):
       hashmap={}

       count_lst=[[]for i in range(len(nums) + 1 )]

       ret_lst=[]
       for n in nums:
         hashmap[n]=hashmap.get(n,0)+1
       for key,value in hashmap.items():
         count_lst[value].append(key) 

       for i in range(len(count_lst) -1,0,-1):
        for j in count_lst[i]:
            ret_lst.append(j)
            if k==len(ret_lst):
                return ret_lst




        