# Logic-2 > lucky_sum
# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.


# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1


def lucky_sum(a, b, c):
  ans = 0
  arr = [a,b,c]
  i = 0
  while i < len(arr):
    if arr[i] != 13:
      ans += arr[i]
    else:
      break
    i += 1
  return ans
