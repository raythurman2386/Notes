"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # set up a hash table
        my_table = {}

        # for each index in the length of nums
        for index in range(len(nums)):
            # if nums[index] is not in the table
            if nums[index] not in my_table:
                # add to the table
                # target - number is the key, with the index as the value
                my_table[target-nums[index]] = index
            else:
                # return the value and the index of where that value is in the list
                return my_table[nums[index]], index


"Test Cases"
"""
[2, 7, 11, 15], 9
[3,2,4], 6
"""
