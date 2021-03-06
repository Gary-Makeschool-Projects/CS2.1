#!python


# local Python Modules
from utils.benchmark import time_it
from utils.swapitems import swap
from utils.bitops import greater


@time_it  # benchmark
def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.

    Runtime: O(n): We have to loop through the array at least n times to check to 
    see if each item is sorted

    Memory usage: O(1) we do not modify or create any more memory than was already allocated"""

    length = items.__len__()
    # Array has one or no element
    if length == 0 or length == 1:  # 1
        return True
    for i in range(1, length):  # n - 1
        # Unsorted pair found
        if (items[i-1] > items[i]):  # n
            return False
    # No unsorted pair found
    return True


@time_it  # benchmark
def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.

    Running time: n*n/2 --> O(n^2) for each item we are checking if the previous is also sorted making the 
    algorithm exponentially propotional to the input size

    Memory usage: O(1) We are modifying the original array not making a copy so 
          the algorithm takes up no additional space than that was already allocated"""

    sorted = False  # is the array sorted
    last = len(items) - 1  # last item sorted is always at the end
    # dont break until the array is sorted
    while not sorted:
        sorted = True
        # for each item in the array
        for i in range(last):
            # bitwise calculation
            # greater()
            if items[i] > items[i+1]:
                # swap values
                swap(items, i, i+1)
                sorted = False
        # decrement is sorted by last value or left value
        last -= 1
    return items


@time_it  # benchmark
def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.

    Running time: O(n^2) sorts an array by repeatedly 
    finding the minimum element (considering ascending order) 
    from unsorted part and putting it at the beginning. 
    Maintaing two given arrays.

    Memory usage: O(1) there is no addtional space given"""

    length = items.__len__()
    # Traverse through all array elements
    for i in range(length):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, length):
            # bitwise calculation
            # greater()
            if items[min_idx] > items[j]:
                # min index
                min_idx = j
        # Swap the found minimum element with the first element
        swap(items, i, min_idx)


@time_it  # benchmark
def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.

    Running time: O(n^2) or O(n*(n-1)) for each item we have to compare to every other item in the array minus the previous ammount hence n-1 

    Memory usage: O(1) We do not allocate any more memory than that was already given"""

    length = items.__len__()
    # Traverse through 1 to length
    for i in range(1, length):
        # key is the current value
        key = items[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        # bitwise calculation
        # greater()
        while j >= 0 and key < items[j]:
            items[j+1] = items[j]
            j -= 1
        items[j+1] = key
