"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
"""

def topKFrequent(nums: list[int], k: int) -> list[int]:
    from collections import defaultdict
    

    counter = defaultdict(int)

    for num in nums:
        counter[num] += 1
    
    return [num for num, _ in sorted(counter.items(), key=lambda x:x[1], reverse=True)[:k]]

print(topKFrequent([1,2,2,3,3,3], 2))