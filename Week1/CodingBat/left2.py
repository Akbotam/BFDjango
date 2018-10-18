def left2(str):
  if len(str) == 2:
    return str
  else:
    front = str[2:]
    return front + str[:2]