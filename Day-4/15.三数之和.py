class Solution:
    def threeSum(self, nums):
        ans = []
        nums.sort()  # 对数组进行排序
        n = len(nums)
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 跳过重复的 i
            
            x = nums[i]
            j, k = i + 1, n - 1  # 双指针初始化
            
            while j < k:
                s = x + nums[j] + nums[k]
                
                if s < 0:
                    j += 1  # 总和小于0，移动左指针
                elif s > 0:
                    k -= 1  # 总和大于0，移动右指针
                else:
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # 跳过重复的 j 和 k
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return ans
sol = Solution()
print(sol.threeSum([-1,0,1]))