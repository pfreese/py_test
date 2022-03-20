def front_back(str):
  if len(str) < 2:
    return str
  n = len(str)
  first_char = str[0]
  last_char = str[n-1]
  middle_chars = str[1:(n-1)]
  return last_char + middle_chars + first_char
