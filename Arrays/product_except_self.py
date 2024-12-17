"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Input: nums = [1,2,4,6]

Output: [48,24,12,8]
"""

def product_except_self(nums: list[int]) -> list[int]:
    product_except_self_array = [1]*len(nums)

    #Initiliaze previous products
    previous_product = 1

    for curr_idx, num in enumerate(nums):
        #check if current number is start of index
        if nums.index(num) == 0:
            previous_product = 1
        else:
            previous_product *= nums[curr_idx - 1] # only multiply up until current number

        #Initiliaze right index after current index
        right_index = curr_idx + 1
        # Initialize variable to hold all product after current nnumber
        right_product = 1
        
        #Multiply all products to the right of current number
        while right_index < len(nums):
            right_product *= nums[right_index]
            right_index += 1
        # Compute all product except self
        all_product_except_self = previous_product * right_product
        # replace current index of output array with all products except self
        product_except_self_array[curr_idx] = all_product_except_self

    return product_except_self_array



print(product_except_self([1,2,4,6]))