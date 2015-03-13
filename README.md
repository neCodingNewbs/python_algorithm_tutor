# Algorithm Tutorial - Python
##What you'll need to start:
###1) Python

 Choose the appropriate OS:
    - https://www.python.org/downloads/

###2) Text Editor

-Atom https://atom.io/

-Sublime Text http://www.sublimetext.com/3

-Or your favorite editor

##Algorithm Tutorial

  We'll look at algorithms to perform 2 of most common processes when dealing with
  data:

  **searching** and **sorting**.



#Sorting

  Sorting often needs to be done before searching.

  Imagine you are creating a phonebook (see Wikipedia to learn what that is ;):

  You have 10,000 people to put in the book and you want to organize them by name.
  By first organising the names(in this case alphabetically), finding a specific
  name later will be much easier.

  We'll look at 3 different sorting algorithms and compare their efficiency.

    -Selection Sort

    -Bubble Sort

    -Merge Sort

##Selection Sort
(http://en.wikipedia.org/wiki/Selection_sort)

  1) Find the smallest item. Swap it with the first item.

  2) Find the second-smallest item. Swap it with the second item.

  3) Find the third-smallest item. Swap it with the third item.

  4) Repeat, finding the next-smallest item, and swapping it into the correct
     position until the array is sorted.

![alt text](https://github.com/theloniusmonkey/python_algorithm_tutor/blob/master/images/selection.JPG)

  Selection sort has a complexity of *O(n^2)*. This means as the number (n) of elements
  in your database increases, the time to sort the database in the worst case
  increases by *n squared*.

  So a 10 item list might take 0.1 seconds to sort.

  A 1000 item list might take ~15 minutes to sort.

  A 1,000,000 list would take more than 30 years to sort!!!!


###Python code

```python
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
```

##Bubble Sort

  The aim again, is to sort from lowest to highest.

  1) Compare the first 2 items, if they are out of order, swap them.

  2) Compare the next two items, if they are out of order, swap them.

  3) Continue until you reach the end of the list.

  4) Starting at the 2nd item, continue from Step 1. (Then 3rd item, etc.)

###Here's a video demonstrating bubble sort.

  <a href = "https://www.youtube.com/watch?v=MtcrEhrt_K0">Lego Bubble Sort
  </a>

  Bubble sort has the same complexity as Selection Sort, so we don't gain
  in efficiency.

```python
def bubbleSort(alist):
  for passnum in range(len(alist)-1,0,-1):
    for num in range(passnum):
      if alist[num]>alist[num+1]:
        temp = alist[num]
        alist[num] = alist[num+1]
        alist[num+1] = temp

```

##Merge Sort

 Merge Sort is the first algorithm we'll look at that demonstrates a real gain
 in efficiency.

 The complexity of merge sort is O(n log n).

 This means that if you had 32 items:

 log (base 2) 32 = 5

 So 5 * 32 = 156 or **0.156 seconds** in the worst case scenario.

 Performing a bubble sort on 32 items would take **1 second** (or 7 times longer).

 Or, a 10000 item list would take almost *28 hours to sort using bubble sort.*

 The same 10000 item list would only take *2.25 minutes* to sort using merge sort.

 Merge sort is a little more complicated, here are the steps:

  1) If the list has more than 1 element, split it half.

  2) Loop back to Step 1.

  3) Otherwise compare two lists and merge them.

  4) Put the smaller item first in the new merged list.

  5) Loop back to 3.

![alt text](https://github.com/theloniusmonkey/python_algorithm_tutor/blob/master/images/merge_sort_recursion.png)

```python
def mergeSort(alist):
  print("Splitting ",alist)
  if len(alist)>1:
    mid = len(alist)//2
    lefthalf = alist[:mid]
    righthalf = alist[mid:]

    mergeSort(lefthalf)
    mergeSort(righthalf)

    i=0
    j=0
    k=0
    while i<len(lefthalf) and j<len(righthalf):
      if lefthalf[i]<righthalf[j]:
        alist[k]=lefthalf[i]
        i=i+1
      else:
        alist[k]=righthalf[j]
        j=j+1
        k=k+1

    while i<len(lefthalf):
      alist[k]=lefthalf[i]
      i=i+1
      k=k+1

    while j<len(righthalf):
      alist[k]=righthalf[j]
      j=j+1
      k=k+1
    print("Merging ",alist)
```
#Searching

  Searching is really the name of the game- we're mainly interested in sorting,
  so that our searching goes better.

  Computers hold data, a *lot* of data. We need efficient ways to find a particular
  piece of information before the universe dies a heat death.

  We'll  compare 2 search algorithms, one that increases linearly in complexity
  O(n), and a second that increases by O(log n).

##Linear Search

  There isn't much to this one. You go through the list, one item at a time until
  you find the item you're looking for. In the worst case scenario, your item is
  at the end of the list.

```python
def linearSearch(item, alist):
  position = 0
  found = False
  while position < len(alist) and not found:
    if alist[position] == item:
      found = True
    position = position + 1
  return found
```
This code returns 'True'  or 'False' if the item is in the list.


##Binary Search

 Binary search is a huge improvement over linear search. It's complexity is of
 the order O(log n).

 In the worst case, a 1,000,000 item list might take *15 minutes* to search using
 linear search.

 Using binary search, the same list would only take *0.02 seconds* to search.

 The pseudocode look like this:

 1) Let min = 0 and max = n-1.

 2) Compute guess as the average of max and min, rounded down (so that it is an integer).

 3) If array[guess] equals target, then stop. You found it! Return guess.

 4) If the guess was too low, that is, array[guess] < target, then set min = guess + 1.

 5) Otherwise, the guess was too high. Set max = guess - 1.

 6) Go back to step 2.

![alt text](https://github.com/theloniusmonkey/python_algorithm_tutor/blob/master/images/binary.jpg)

```python
def binarySearch(alist, item):
  first = 0
  last = len(alist)-1
  found = False

  while first<=last and not found:
    midpoint = (first + last)//2
    if alist[midpoint] == item:
      found = True
    else:
      if item < alist[midpoint]:
        last = midpoint-1
      else:
        first = midpoint+1

  return found
```

One thing to notice about these search algorithms is that they require the lists
to be sorted first. So if you have a huge jumble of data, first you need to sort it.
However, once sorted, searches can be performed repeatedly and quickly.
