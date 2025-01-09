# String-2 > cat_dog
# Return True if the string "cat" and "dog" appear the same number of times in the given string.
#
#
# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True


def cat_dog(str):
  c_count = 0
  d_count = 0
  for i in range(len(str)):
    if str[i:i+3] == 'cat':
      c_count += 1
    if str[i:i+3] == 'dog':
      d_count += 1
  if c_count == d_count:
    return True
  return False
