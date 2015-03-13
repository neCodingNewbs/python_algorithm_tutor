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
  data: *searching* and *sorting*.




#Sorting
  Sorting often needs to be done before searching.

  Imagine you are creating a phonebook (see Wikipedia t0 learn what that is ;):

  You have 10,000 people to put in the book and you want to organize them by name.
  By organising the names(in this case alphabetically), finding a specific
  name later will be much easier.

  We'll look at 3 different sorting algorithms and compare their efficiency.

    -Selection Sort

    -Bubble Sort

    -Merge Sort

##Selection Sort
(http://en.wikipedia.org/wiki/Selection_sort)

  1) Find the smallest card. Swap it with the first card.

  2) Find the second-smallest card. Swap it with the second card.

  3) Find the third-smallest card. Swap it with the third card.

  4) Repeat finding the next-smallest card, and swapping it into the correct
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

  The aim is to sort from lowest to highest.

  1) Compare the first 2 items, if they are out of order, swap them.

  2) Compare the next two items, if they are out of order, swap them.

  3) Continue until you reach the end of the list.

  4) Starting at the 2nd item, continue from Step 1. (Then 3rd item, etc.)

  <a href = "https://www.youtube.com/watch?v=MtcrEhrt_K0">
![alt text](https://github.com/theloniusmonkey/python_algorithm_tutor/tree/master/images/lego.jpg)
  </a>
