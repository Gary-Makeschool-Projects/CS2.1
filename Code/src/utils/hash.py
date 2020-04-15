import math

""" little hashing alogrimth"""


def hashing(A):
    m = A[0]
    for i in range(1, len(A)):
        if (m < A[i]):
            m = A[i]
    result = [m, int(math.sqrt(len(A)))]
    return result
