def linearSearch(item, alist):
  position = 0
  found = False
  while position < len(alist) and not found:
    if alist[position] == item:
      found = True
    position = position + 1
  return found

alist = [54,26,93,17,77,31,44,55,20]
print(linearSearch(31, alist))
print(linearSearch(1, alist))
