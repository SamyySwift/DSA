"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""

def contains_duplicate(nums: list[int]) -> bool:
    counter = {}

    for n in nums:
        counter[n] = 1 + counter.get(n,0)

    return max(counter.values()) > 1




print(contains_duplicate([1,2,3,4]))