def is_perfect_square(n):
    if n <= 0:          # Line 1
        return False    # Line 2
    if n == 1:          # Line 3
        return True     # Line 4

    low = 2             # Line 5
    high = n            # Line 6   # Should be n // 2 ??

    while low <= high:              # Line 7
        mid = (low + high) // 2     # Line 8
        mid_sq = mid * mid          # Line 9

        if mid_sq == n:             # Line 10
            return True             # Line 11
        elif mid_sq < n:            # Line 12
            low = mid + 1           # Line 13
        else:                       # Line 14
            high = mid - 1          # Line 15

    return False                    # Line 16