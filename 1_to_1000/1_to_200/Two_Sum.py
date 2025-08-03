class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            index1 = nums.index(num)
            searched_num = target - num
            for index2 in range(index1 + 1,len(nums)):
                if nums[index2] == searched_num:
                    return(index1, index2)
        return None
