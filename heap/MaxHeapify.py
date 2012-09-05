from Util import *

def left(i):
    return i*2

def right(i):
    return i*2 + 1

def max_heapify(arr, i, heap_size):
    largest = 0
    if left(i) <= heap_size and arr[left(i)] > arr[i]:
        largest = left(i)
    else:
        largest = i
    if right(i) <= heap_size and arr[right(i)] > arr[largest]:
        largest = right(i)


    if largest != i:
        swap(arr, largest, i)
        #print arr[1:]
        max_heapify(arr, largest, heap_size)

if __name__ == '__main__':
    dumb = -1
    array = [dumb, 27, 17, 3 ,16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0];
    print "before:", array[1:]
    global heap_size
    heap_size = len(array)
    max_heapify(array, 3, len(array))
    print "after:", array[1:]
