# List-1 > max_end3
# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.


# max_end3([1, 2, 3]) → [3, 3, 3]
# max_end3([11, 5, 9]) → [11, 11, 11]
# max_end3([2, 11, 3]) → [3, 3, 3]


def max_end3(nums):
  larger = nums[0] if nums[0] > nums[-1] else nums[-1]
  for i in range(len(nums)):
    nums[i] = larger
  return nums
