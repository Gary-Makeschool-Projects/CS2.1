#!python

# built-in Python Modules
from random import randint

# local Python Modules
from sorting_iterative import bubble_sort, insertion_sort, selection_sort
from sorting_integer import counting_sort_int
from utils.benchmark import time_it
from utils.swapitems import swap


@time_it  # benchmark
def next_gap(gap):
    """Reducing the gap by a factor of 2"""

    if gap <= 1:

        return 0

    res = (gap // 2) + (gap % 2)

    return res


def split(arr):
    """Get the midpoint of an array"""

    l = len(arr)

    mid = (l // 2)

    return mid

#################### helper functions ########################


@time_it  # benchmark
def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.

    Running time: O(n + m) n and m are the lengths of both arrays we at least
    have to cycle through both arrays at least once.

    Memory usage: O(n + m) We create an array of size n + m to fit the contents
    of both arrays inside. The space we need for this operation is linearly
    porportional to both our arrays. """

    size1 = len(items1)
    size2 = len(items2)
    items3 = [None] * (size1 + size2)
    i = 0
    j = 0
    k = 0

    # Traverse both arrays
    while i < size1 and j < size2:

        if items1[i] < items2[j]:
            items3[k] = items1[i]
            k = k + 1
            i = i + 1
        else:
            items3[k] = items2[j]
            k = k + 1
            j = j + 1

    # Store remaining elements
    # of first array
    while i < size1:
        items3[k] = items1[i]
        k = k + 1
        i = i + 1

    # Store remaining elements
    # of second array
    while j < size2:
        items3[k] = items2[j]
        k = k + 1
        j = j + 1

    return items3


@time_it  # benchmark
def merge_tonic(items1, items2):
    """Merge two given list of items. This approach I form two bitonic arrays
    by comparing the highest element from one array to the lowest element of
    the second array such that both arrays contain only those elements which
    are to be there in after the sorting of both the array.

    Running time: O(nlogn + mlogm)

    Memory Usage: O(1) We do not use any additional memory we swap the
    elements in the given arrays
    """

    n = len(items1)
    m = len(items2)
    x = min(n, m)

    # Form both arrays to be bitonic
    for i in range(x):

        if (items1[n - i - 1] > items2[i]):
            # swap
            items1[n - i - 1], items2[i] = items2[i], items1[n - i - 1]

    # Sort the array inplace
    gap = next_gap(n)
    while gap > 0:

        # Comparing elements in the first array
        index = 0

        while index + gap < n:

            if (items1[index] > items1[index + gap]):
                # swap
                items1[index], items1[index +
                                      gap] = items1[index + gap], items1[index]

            index += 1

        gap = next_gap(gap)

    # Sort the second array
    gap = next_gap(m)
    while gap > 0:

        # Comparing elements in the second array
        index = 0
        while index + gap < m:
            if (items2[index] > items2[index + gap]):
                # swap
                items2[index], items2[index +
                                      gap] = items2[index + gap], items2[index]

            index += 1

        gap = next_gap(gap)

    # this return statment is not needed and goes against the algorithm
    # for constant space time. This is just used to easily diplay the contents.
    # array 1 and array 2 are already sorted. We can call each indivual array
    # to see their contents.
    return items1 + items2


@time_it  # benchmark
def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.

    Running time:  O((nlogn + mlogm) + n) or O((n + m) + n) First counting_sort() average's time
    complexity is O(n) and the there are two merge functions we can call. merge_tonic() is
    more memory efficient but time efficiency is the cost. merge() is more time efficient
    but less space efficient.

    Memory usage: O(1) or O(n + m) The function merge_tonic() takes up no additional
    space when merging the two arrays. merge() creates an array the size of both
    arrays being merged hence n + m"""

    # split
    m = split(items)
    lh = items[:m]
    rh = items[m:]

    # sort
    counting_sort_int(lh)  # O(n)
    counting_sort_int(rh)  # O(n)

    # merge
    return merge_tonic(lh, rh)  # O(nlogn + mlogm)


@time_it  # benchmark
def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.

    Running time: O((nlogn + mlogm) logn) merge_tonic() is not linearly
    proportional to the input size. Its nlogn + mlogm such that it resides in the set nlogn + c.

    Memory usage: O(1) merge_tonic() does not use any additional memory we swap the
    elements in the given arrays"""

    # base case and only case
    if len(items) > 1:

        # split the array down the middle
        m = split(items)

        # arrays left half
        lh = items[:m]

        # arrays right half
        rh = items[m:]

        # recursivley call merge_sort() on other halfs
        merge_sort(lh)
        merge_sort(rh)

        # reassign all values
        items[:] = merge_tonic(lh, rh)


def partition(items, l, h):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot from that range, moving pivot into index
    `p`, items less than pivot into range `[low...p-1]`, and items
    greater than pivot into range `[p+1...high]`.

    Running time: O(n logn)

    Memory usage: O(1) We never allocate any more memory than was already given
    except a few constant variables"""

    p_idx = randint(l, h)
    items[p_idx], items[l] = items[p_idx], items[l]
    p = items[l]
    low = l + 1
    high = h

    while True:
        # if larger than the pivot we can move to the next element
        while low <= high and items[high] >= p:
            high -= 1
        # if smaller than the pivot
        while low <= high and items[low] <= p:
            low += 1

        if low <= high:
            # swap
            swap(items, low, high)

        else:
            break

    items[l], items[high] = items[high], items[l]

    return high


@time_it  # benchmark
def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: O(n)
    Worst case running time: O(n logn)
    Memory usage: O(logn)"""
    if low is None and high is None:
        low = 0
        high = len(items) - 1

    if low < high:
        # partition the items
        p = partition(items, low, high)
        # sort both half of the partition recursively
        quick_sort(items, low, p-1)
        quick_sort(items, p+1, high)
