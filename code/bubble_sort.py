def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for num in range(passnum):
            if alist[num]>alist[num+1]:
                temp = alist[num]
                alist[num] = alist[num+1]
                alist[num+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
print(alist)
bubbleSort(alist)
print(alist)
