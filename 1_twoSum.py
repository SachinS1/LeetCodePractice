from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force 
        # output=[]
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             output.append(i)
        #             output.append(j)
        # return output

        # hashmap to keep a record of visited numbers
        hash_store = {} 
        
        for i, n in enumerate(nums):
            diff = target - n
        
            if diff in hash_store:
                return [hash_store[diff], i]
            hash_store[n] = i # update the hashmap with a newest value

        return
    
