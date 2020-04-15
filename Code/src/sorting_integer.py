#!python

# local Python Modules
from utils.benchmark import time_it
from utils.hash import hashing


@time_it  # benchmark
def counting_sort_int(array):
    """The lower bound Ω(n log n) does not apply to algorithms
    that do not compare array elements but use some other
    information. Can only be used when the constant c is small enough,
    so that the array elements can be used as indices
    in the bookkeeping array.

    Best case running time: O(n) assuming that every element in the array
    is an integer between 0-c such that c = O(n)

    Average case running time: O(n) assuming that every element in the array
    is an integer between 0-c such that c = O(n)

    Worst case running time: O(n^c) if c is a very large integer
    that is not within the range of 0-c such that c ≠ O(n)

    Memory usage: O(1) We use a partial hashing algorithm to count
    the occurrence of the data.  """

    size = len(array)

    # The output integer array that will have the sorted array
    output = [0] * size

    # Hash array
    count = [0] * 10

    # Create a count array to store count of individual
    # integers and initialize count array as 0
    for i in range(size):
        count[array[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(size):
        array[i] = output[i]


@time_it  # benchmark
def counting_sort_strings(items):
    """The lower bound Ω(n log n) does not apply to algorithms
    that do not compare array elements but use some other
    information. Can only be used when the constant c is small enough,
    so that the array elements can be used as indices
    in the bookkeeping array.

    Best case running time: O(n) assuming that every element in the array
    is an integer between 0-c such that c = O(n)

    Average case running time: O(n) assuming that every element in the array
    is an integer between 0-c such that c = O(n)

    Worst case running time: O(n^c) if c is a very large integer
    that is not within the range of 0-c such that c ≠ O(n)

    Memory usage: O(1) We use a partial hashing algorithm to count
    the occurrence of the data.  """
    # The output character array that will have sorted arr
    output = [0 for i in range(256)]

    # Create a count array to store count of inidividul
    # characters and initialize count array as 0
    count = [0 for i in range(256)]

    # For storing the resulting answer since the
    # string is immutable
    ans = ["" for _ in items]

    # Store count of each character
    for i in items:
        count[ord(i)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i-1]

    # Build the output character array
    for i in range(len(items)):
        output[count[ord(items[i])]-1] = items[i]
        count[ord(items[i])] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(items)):
        ans[i] = output[i]

    return ans


def bucket_sort(arr):
    # get hash codes
    code = hashing(arr)
    buckets = [list() for _ in range(code[1])]

    # distrubute items into buckets
    for i in arr:
        x = re_hashing(i, code)
        buck = buckets[x]
        buck.append(i)

    for bucket in buckets:
        counting_sort_int(bucket)

    ndx = 0
    # merge the buckets: O(n)
    for b in range(len(buckets)):
        for v in buckets[b]:
            A[ndx] = v
            ndx += 1


def re_hashing(i, code):
    return int(i / code[0] * (code[1] - 1))
