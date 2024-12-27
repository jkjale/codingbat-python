# String-1 > non_start
# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.


# non_start('Hello', 'There') → 'ellohere'
# non_start('java', 'code') → 'avaode'
# non_start('shotl', 'java') → 'hotlava'


def non_start(a, b):
  new_a = ''
  new_b = ''
  if len(a) > 1:
    new_a = a[1:]
  if len(b) > 1:
    new_b = b[1:]
  return new_a + new_b
