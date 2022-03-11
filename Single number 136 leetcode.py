"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.


Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""


def singleNumber(nums):
    single_Number = [x for x in nums if nums.count(x) == 1]
    return single_Number[0]

    # for n in nums:
    #     if nums.count(n) == 1:
    #         print(n)
    #         return n


if __name__ == '__main__':
    assert singleNumber([2, 2, 1]) == 1
    assert singleNumber([4, 1, 2, 1, 2]) == 4
    assert singleNumber([1]) == 1
