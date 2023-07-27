# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

nums = [2,7,11,15]
target = 9


def twoSum(self, nums: list[int], target: int) -> list[int]:

        d = {}

        for index, val in enumerate(nums):

            rem = target - val

            if rem in d: return [d[rem], index]

            d[val] = index

twoSum()



