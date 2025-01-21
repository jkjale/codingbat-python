# List-2 > sum67
# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
#
#
# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4


def sum67(nums):
  ind = []
  inds = []
  final_inds = []
  ans = []
  is_six = False
  for i in range(len(nums)):
    if nums[i] == 6:
      if is_six:
        continue
      else:
        is_six = True
        ind.append(i)
    if nums[i] == 7:
      if is_six:
        ind.append(i)
        is_six = False
      else:
        continue
  for i in range(0,len(ind),2):
    inds.append(ind[i:i+2])
  for arr in inds:
    for i in range(arr[0],arr[1]+1):
      final_inds.append(i)
  for i in range(len(nums)):
    if i not in final_inds:
      ans.append(nums[i])
  return sum(ans)
