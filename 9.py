def is_anagram(str1, str2):
  if len(str1) != len(str2):
    return False
  char_counts = {}
  for char in str1:
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1

  for char in str2:
    if char not in char_counts:
      return False
    char_counts[char] -= 1

  for count in char_counts.values():
    if count != 0:
      return False

  return True

str1 = 'coding'
str2 = 'ingodc'
print(is_anagram(str1, str2))

str1 = 'hello'
str2 = 'hoeli'
print(is_anagram(str1, str2))
