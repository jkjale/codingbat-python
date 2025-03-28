# String-2 > end_other
# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
#
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
  low_a = a.lower()
  low_b = b.lower()
  shorter = low_a if len(a) < len(b) else low_b
  longer = low_b if len(a) < len(b) else low_a
  if longer[-len(shorter):] == shorter:
    return True
  return False

