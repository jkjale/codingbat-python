# Logic-2 > lone_sum
# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.


# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0


def lone_sum(a, b, c):
  map1 = {}
  arr = [a,b,c]
  ans = 0
  for num in arr:
    if num in map1:
      map1[num] = 2
    else:
      map1[num] = 1
  for key,val in map1.items():
    if val < 2:
      ans += key
  return ans
