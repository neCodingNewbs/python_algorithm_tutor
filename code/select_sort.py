def selection_sort(aList):
  for n in range(len(aList)):
    least = n
    for number in range(n + 1 , len(aList)):
      if aList[number] < aList[least]:
        least = number

    swap(aList, least, n)


def swap(array, x, y):
  temp = array[x]
  array[x] = array[y]
  array[y] = temp


aList = [2,9,4,1,6,7,8,3,10,5]
print aList
selection_sort(aList)
print aList
