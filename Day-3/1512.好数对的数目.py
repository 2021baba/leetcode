class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]==nums[j]:
                    result=result+1
