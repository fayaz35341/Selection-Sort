class Solution:
    def selectionSort(self, nums):
        for i in range(len(nums)):
            minV =i 
            for j in range(len(nums)-1):
                if nums[i]>nums[j]:
                    nums[minV],nums[j] = nums[j],nums[minV]
        return nums
n=input().strip("[]")
n=list(map(int,n.split(",")))
print(Solution().selectionSort(n))

#Input: nums = [7, 4, 1, 5, 3]
#Output: [7, 5, 4, 3, 1]
