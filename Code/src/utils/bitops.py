
def greater(a, b):
    if isinstance(a, int) and isinstance(b, int):
        ltb = ~a & b
        gtb = a & ~b

        ltb |= ltb >> 1
        ltb |= ltb >> 2
        ltb |= ltb >> 4
        ltb |= ltb >> 8
        ltb |= ltb >> 16
        isGt = gtb & ~ltb
        isGt |= isGt >> 1
        isGt |= isGt >> 2
        isGt |= isGt >> 4
        isGt |= isGt >> 8
        isGt |= isGt >> 16
        isGt &= 1
        return isGt
    else:
        return "not an integer"
