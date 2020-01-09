class Solution:
    def search(self, nums, target):
        index_int = (len(nums)-1) // 2
        return self.searchHelper(nums, target, index = index_int)
    
    def searchHelper(self, nums, target, index):
        if len(nums) == 0:
            return -1
        
        idx = index
        mid = (len(nums)-1)//2
        if nums[mid] == target:
            return idx
        else:
            if target < nums[mid]: 
                less_length = len(nums[0:mid])
                return self.searchHelper(nums[:mid], target, idx-(less_length+2)//2)
            if target > nums[mid]:
                larger_length = len(nums[mid+1:])
                return self.searchHelper(nums[mid+1:], target, idx+(larger_length+1)//2)
