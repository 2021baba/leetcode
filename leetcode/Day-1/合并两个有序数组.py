class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                nums2.remove(nums2[i])
        temp =0
        nums1 = nums1 + nums2
        for j in range(len(nums1)):
            if nums1[j]>=nums1[j+1]:
                temp = nums1[j]
                nums2[j] = nums2[j+1]
                nums2[j+1]=temp

