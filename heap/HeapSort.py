from Util import *
from BuildMaxHeap import *

def test():
    arr = gen_data()
    swap(arr, 1, 2)
    print "test",arr

if __name__ == '__main__':
    array = gen_data()

    #start sort.
    heap_size = len(array) - 1
    build_max_heap(array)
    for i in reversed(xrange(2, len(array))):
        swap(array, 1, i)
        heap_size -= 1
        max_heapify(array, 1, heap_size)

    print array
