# List-2 > sum13
# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
#
#
# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6


def sum13(nums):
  ind = []
  ans = 0
  for i in range(len(nums)):
    if nums[i] == 13:
      ind.append(i)
      ind.append(i+1)
  for i in range(len(nums)):
    if i not in ind:
      ans += nums[i]
  return ans