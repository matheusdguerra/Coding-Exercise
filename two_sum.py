"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


def twoSum(nums, target):
    for idx1, n1 in enumerate(nums):
        for idx2, n2 in enumerate(nums):
            print([idx1, idx2])
            print(n1, n2, target)
            if n1 + n2 == target and idx1 != idx2:
                return [idx1, idx2]


if __name__ == '__main__':
    assert twoSum([2, 7, 11, 15], 9,) == [0, 1]
    assert twoSum([3, 2, 4], 6,) == [1, 2]
    assert twoSum([3, 3], 6,) == [0, 1]
    assert twoSum([2, 5, 5, 11], 10,) == [1, 2]
