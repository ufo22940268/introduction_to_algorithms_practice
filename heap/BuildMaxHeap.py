from MaxHeapify import *

def pretty_print(array):
    print range(0, len(array))
    for i, j in zip(range(len(array)), array):
            print str(i) + ":" + str(j)

def build_max_heap(array):
    for i in reversed(range(1, len(array)/2)):
        max_heapify(array, i, len(array))


if __name__ == '__main__':
    nil = -1
    array = [nil, 27, 17, 3 ,16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    build_max_heap(array)
    pretty_print(array)
