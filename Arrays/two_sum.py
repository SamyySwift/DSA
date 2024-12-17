"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
"""

#using Hash map
def two_sum(nums: list[int], target:int) -> list[int, int]:
    hash_map = {}

    for num_indx, num in enumerate(nums):
        diff = target - nums[num_indx]
        if diff in hash_map:
            return hash_map[diff], num_indx
        hash_map[num] = num_indx
        

# Using two pinter approach
def two_sum_pointer(nums: list[int], target: int) -> list[int, int]:
    l, r = 0, len(nums) - 1

    nums.sort()
    print(nums)

    while l != r:
        print(l, r)
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:    
           
            l += 1
        else:
            return l,r
    return "no number"


print(two_sum(nums = [2, 11,15, 7, 8], target = 26))